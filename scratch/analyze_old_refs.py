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

def analyze_old_files(root_dir):
    old_labels = {}  # label_name -> list of (rel_path, line_num, content)
    old_refs = {}    # label_name -> list of (rel_path, line_num, content, ref_type)
    
    # Active/new files labels
    active_labels = {} # label_name -> list of (rel_path, line_num, content)
    
    label_pattern = re.compile(r'\\label\{([^}]+)\}')
    # Match standard and custom reference macros
    ref_pattern = re.compile(r'\\(ref|pageref|cref|Cref|figref|tabref|eqnref|chapref|secref)\{([^}]+)\}')
    
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
                                if lbl not in active_labels:
                                    active_labels[lbl] = []
                                active_labels[lbl].append(loc_info)
                                
                        # Find refs
                        if is_old:
                            for match in ref_pattern.finditer(clean_line):
                                ref_type = match.group(1)
                                ref_target_str = match.group(2).strip()
                                for r in ref_target_str.split(','):
                                    r = r.strip()
                                    if not r or r.startswith('#') or r.startswith('\\'):
                                        continue
                                    ref_info = (rel_path, line_num, line.strip(), ref_type)
                                    if r not in old_refs:
                                        old_refs[r] = []
                                    old_refs[r].append(ref_info)
                                    
    return old_labels, old_refs, active_labels

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"Analyzing cross-references within OLD files in: {root_dir}\n")
    
    old_labels, old_refs, active_labels = analyze_old_files(root_dir)
    
    print(f"Total labels defined in OLD files: {len(old_labels)}")
    print(f"Total references used in OLD files: {len(old_refs)}")
    print()
    
    print("=== CROSS-REFERENCE TARGET ANALYSIS FOR OLD FILES ===")
    
    resolved_in_old = []
    resolved_in_active = []
    unresolved_everywhere = []
    
    for ref_name, ref_locs in old_refs.items():
        if ref_name in old_labels:
            resolved_in_old.append((ref_name, ref_locs, old_labels[ref_name]))
        elif ref_name in active_labels:
            resolved_in_active.append((ref_name, ref_locs, active_labels[ref_name]))
        else:
            unresolved_everywhere.append((ref_name, ref_locs))
            
    print(f"1. References resolved within OLD files themselves: {len(resolved_in_old)}")
    if resolved_in_old:
        for ref_name, ref_locs, def_locs in resolved_in_old:
            print(f"  - '{ref_name}'")
            print(f"    Referenced at:")
            for loc in ref_locs:
                print(f"      * {loc[0]}:{loc[1]} via \\{loc[3]}: `{loc[2]}`")
            print(f"    Defined at:")
            for loc in def_locs:
                print(f"      * {loc[0]}:{loc[1]}: `{loc[2]}`")
            print()
            
    print(f"2. References in OLD files pointing to ACTIVE files: {len(resolved_in_active)}")
    if resolved_in_active:
        for ref_name, ref_locs, def_locs in resolved_in_active:
            print(f"  - '{ref_name}'")
            print(f"    Referenced at:")
            for loc in ref_locs:
                print(f"      * {loc[0]}:{loc[1]} via \\{loc[3]}: `{loc[2]}`")
            print(f"    Defined at (in active files):")
            for loc in def_locs:
                print(f"      * {loc[0]}:{loc[1]}: `{loc[2]}`")
            print()
            
    print(f"3. Broken/Unresolved references in OLD files (not defined anywhere): {len(unresolved_everywhere)}")
    if unresolved_everywhere:
        for ref_name, ref_locs in unresolved_everywhere:
            print(f"  - '{ref_name}' (WARNING: Undefined target!)")
            print(f"    Referenced at:")
            for loc in ref_locs:
                print(f"      * {loc[0]}:{loc[1]} via \\{loc[3]}: `{loc[2]}`")
            print()
            
if __name__ == "__main__":
    main()
