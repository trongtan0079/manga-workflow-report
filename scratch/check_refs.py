import os
import re
import sys

# Ensure UTF-8 output encoding for terminal printing
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def remove_comments(line):
    parts = re.split(r'(?<!\\)%', line)
    return parts[0]

def parse_tex_files(root_dir):
    labels = {} # label_name -> list of (file, line_num, content)
    refs = {}   # ref_name -> list of (file, line_num, content, ref_type)
    
    label_pattern = re.compile(r'\\label\{([^}]+)\}')
    ref_pattern = re.compile(r'\\(ref|pageref|cref|Cref|figref|tabref|eqnref|chapref|secref)\{([^}]+)\}')
    
    for root, dirs, files in os.walk(root_dir):
        if any(d in root for d in ['.git', 'docs', 'UML', 'assets']):
            continue
        for file in files:
            if file.endswith('.tex'):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, root_dir)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    for line_num, line in enumerate(f, 1):
                        clean_line = remove_comments(line)
                        
                        # Find labels
                        for match in label_pattern.finditer(clean_line):
                            lbl = match.group(1).strip()
                            if lbl not in labels:
                                labels[lbl] = []
                            labels[lbl].append((rel_path, line_num, line.strip()))
                            
                        # Find refs
                        for match in ref_pattern.finditer(clean_line):
                            ref_type = match.group(1)
                            ref_target_str = match.group(2).strip()
                            for r in ref_target_str.split(','):
                                r = r.strip()
                                if not r or r.startswith('#') or r.startswith('\\'):
                                    continue
                                if r not in refs:
                                    refs[r] = []
                                refs[r].append((rel_path, line_num, line.strip(), ref_type))
                                
    return labels, refs

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"Scanning LaTeX files in: {root_dir}\n")
    
    labels, refs = parse_tex_files(root_dir)
    
    # 1. Check duplicate labels
    duplicates = {lbl: locs for lbl, locs in labels.items() if len(locs) > 1}
    print("=== 1. DUPLICATE LABELS ===")
    if duplicates:
        for lbl, locs in duplicates.items():
            print(f"Label '{lbl}' is defined {len(locs)} times:")
            for loc in locs:
                print(f"  - {loc[0]}:{loc[1]}: `{loc[2]}`")
    else:
        print("No duplicate labels found.")
    print()

    # 2. Check undefined references
    undefined = []
    for ref_name, ref_locs in refs.items():
        if ref_name not in labels:
            undefined.append((ref_name, ref_locs))
            
    print("=== 2. UNDEFINED REFERENCES ===")
    if undefined:
        for ref_name, ref_locs in undefined:
            print(f"Reference '{ref_name}' is undefined. Used at:")
            for loc in ref_locs:
                print(f"  - {loc[0]}:{loc[1]} via \\{loc[3]}: `{loc[2]}`")
    else:
        print("No undefined references found.")
    print()

    # 3. Check unused labels
    unused = []
    for lbl, locs in labels.items():
        if lbl not in refs:
            unused.append((lbl, locs))
            
    print("=== 3. UNUSED LABELS ===")
    print(f"Found {len(unused)} unused labels out of {len(labels)} total labels.")
    print()

if __name__ == "__main__":
    main()
