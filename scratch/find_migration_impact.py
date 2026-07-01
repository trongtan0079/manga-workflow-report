import os
import re
import sys

# Ensure UTF-8 output encoding for terminal printing
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

OLD_FILES = {
    r'chapters\02_1_yeu_cau_chuc_nang.tex',
    r'chapters\02_2_yeu_cau_phi_chuc_nang.tex',
    r'chapters\03_2_uml_nghiep_vu.tex',
    r'chapters\03_3_uml_thiet_ke.tex',
    r'chapters\03_4_database_ui.tex'
}

def remove_comments(line):
    parts = re.split(r'(?<!\\)%', line)
    return parts[0]

def analyze_project(root_dir):
    old_labels = {}  # label_name -> list of (rel_path, line_num, content)
    new_labels = {}  # label_name -> list of (rel_path, line_num, content)
    
    # references: label_name -> list of (rel_path, line_num, content, ref_type)
    old_refs = {}
    new_refs = {}
    
    label_pattern = re.compile(r'\\label\{([^}]+)\}')
    ref_pattern = re.compile(r'\\(ref|pageref|cref|Cref)\{([^}]+)\}')
    
    for root, dirs, files in os.walk(root_dir):
        if any(d in root for d in ['.git', 'docs', 'UML', 'assets']):
            continue
        for file in files:
            if file.endswith('.tex'):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, root_dir)
                is_old = rel_path in OLD_FILES
                
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    for line_num, line in enumerate(f, 1):
                        clean_line = remove_comments(line)
                        
                        # Find labels
                        for match in label_pattern.finditer(clean_line):
                            lbl = match.group(1).strip()
                            loc_info = (rel_path, line_num, line.strip())
                            if is_old:
                                if lbl not in old_labels:
                                    old_labels[lbl] = []
                                old_labels[lbl].append(loc_info)
                            else:
                                if lbl not in new_labels:
                                    new_labels[lbl] = []
                                new_labels[lbl].append(loc_info)
                                
                        # Find references
                        for match in ref_pattern.finditer(clean_line):
                            ref_type = match.group(1)
                            ref_target_str = match.group(2).strip()
                            for r in ref_target_str.split(','):
                                r = r.strip()
                                if not r or r.startswith('#') or r.startswith('\\'):
                                    continue
                                ref_info = (rel_path, line_num, line.strip(), ref_type)
                                if is_old:
                                    if r not in old_refs:
                                        old_refs[r] = []
                                    old_refs[r].append(ref_info)
                                else:
                                    if r not in new_refs:
                                        new_refs[r] = []
                                    new_refs[r].append(ref_info)
                                    
    return old_labels, new_labels, old_refs, new_refs

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"Scanning for migration impact in: {root_dir}\n")
    
    old_labels, new_labels, old_refs, new_refs = analyze_project(root_dir)
    
    # 1. Labels defined ONLY in old files
    only_in_old = set(old_labels.keys()) - set(new_labels.keys())
    
    # 2. Labels defined in BOTH old and new files (potential duplication warning during migration)
    duplicated_across = set(old_labels.keys()) & set(new_labels.keys())
    
    print("=== 1. LABELS DEFINED IN NEW FILES ALREADY ===")
    print(f"Total labels in new files: {len(new_labels)}")
    print(f"Total labels in old files: {len(old_labels)}")
    print()
    
    print("=== 2. DUPLICATED LABELS BETWEEN OLD & NEW FILES ===")
    if duplicated_across:
        print("These labels exist in BOTH old and new files. Make sure they are not defined twice in active compilation:")
        for lbl in sorted(duplicated_across):
            print(f"Label '{lbl}':")
            for loc in old_labels[lbl]:
                print(f"  [OLD] - {loc[0]}:{loc[1]}: `{loc[2]}`")
            for loc in new_labels[lbl]:
                print(f"  [NEW] - {loc[0]}:{loc[1]}: `{loc[2]}`")
    else:
        print("No duplicated labels between old and new files.")
    print()
    
    print("=== 3. CRITICAL REFERENCES: REFERENCES IN NEW FILES POINTING TO OLD LABELS ===")
    critical_refs_count = 0
    for lbl in sorted(only_in_old):
        if lbl in new_refs:
            critical_refs_count += 1
            print(f"Label '{lbl}' (defined only in old files) is referenced by NEW files:")
            print(f"  Defined at:")
            for loc in old_labels[lbl]:
                print(f"    - {loc[0]}:{loc[1]}: `{loc[2]}`")
            print(f"  Referenced at:")
            for ref in new_refs[lbl]:
                print(f"    - {ref[0]}:{ref[1]} via \\{ref[3]}: `{ref[2]}`")
            print()
    if critical_refs_count == 0:
        print("No new files reference old labels. Good! Migration won't break existing new-file references.")
    print()
    
    print("=== 4. INTRA-OLD REFERENCES: REFERENCES IN OLD FILES POINTING TO OLD LABELS ===")
    intra_refs_count = 0
    for lbl in sorted(only_in_old):
        if lbl in old_refs and lbl not in new_refs:
            intra_refs_count += 1
            print(f"Label '{lbl}' is referenced within OLD files only. Make sure to move these references when migrating content:")
            print(f"  Defined at:")
            for loc in old_labels[lbl]:
                print(f"    - {loc[0]}:{loc[1]}: `{loc[2]}`")
            print(f"  Referenced at:")
            for ref in old_refs[lbl]:
                print(f"    - {ref[0]}:{ref[1]} via \\{ref[3]}: `{ref[2]}`")
            print()
    if intra_refs_count == 0:
        print("No intra-old references found.")
    print()

if __name__ == "__main__":
    main()
