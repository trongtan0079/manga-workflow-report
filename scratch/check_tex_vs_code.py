import os
import re

models_dir = r"d:\LapTrinhWeb\manga-workflow-report\Manga-publishing-management-system\models"
tex_file = r"d:\LapTrinhWeb\manga-workflow-report\chapters\04_3_sdd_detailed.tex"

# 1. Parse PHP models for classes and methods
php_models = {}
for file in os.listdir(models_dir):
    if file.endswith(".php"):
        filepath = os.path.join(models_dir, file)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Find class name
        class_match = re.search(r"class\s+(\w+)\s+extends\s+Model", content)
        if class_match:
            class_name = class_match.group(1)
            # Find public methods (including static ones)
            methods = re.findall(r"public\s+(?:static\s+)?function\s+(\w+)\s*\((.*?)\)", content)
            # Ignore constructor
            methods = [m for m in methods if m[0] != "__construct"]
            
            php_models[class_name] = {
                "file": file,
                "methods": {m[0] for m in methods}
            }

# 2. Parse LaTeX file for methods
# Format in LaTeX is like:
# \item \textbf{Lớp Role:}
# \begin{itemize}
#     \item \texttt{findByRoleName(roleName: string): Role}\\
with open(tex_file, "r", encoding="utf-8") as f:
    tex_content = f.read()

# Let's extract each \item \textbf{Lớp ClassName:} block
class_blocks = re.findall(r"\\item\s+\\textbf\{Lớp\s+(\w+):\}(.*?)(?=\\item\s+\\textbf\{Lớp|\Z)", tex_content, re.DOTALL)

tex_classes = {}
for class_name, block in class_blocks:
    # Find all \item \texttt{methodName(...)}
    methods = re.findall(r"\\item\s+\\texttt\{(\w+)\s*\(", block)
    tex_classes[class_name] = set(methods)

# 3. Compare
print("=== COMPARING TEX CLASSES WITH PHP ===")
php_classes = set(php_models.keys())
tex_class_names = set(tex_classes.keys())

print(f"Missing in Tex: {php_classes - tex_class_names}")
print(f"Missing in PHP: {tex_class_names - php_classes}")

print("\n=== COMPARING METHODS BY CLASS ===")
for class_name in sorted(php_classes.union(tex_class_names)):
    if class_name in php_models and class_name in tex_classes:
        php_methods = php_models[class_name]["methods"]
        tex_methods = tex_classes[class_name]
        
        extra_in_php = php_methods - tex_methods
        extra_in_tex = tex_methods - php_methods
        
        print(f"\nClass {class_name}:")
        if extra_in_php:
            print(f"  [+] In PHP but not in Tex: {extra_in_php}")
        if extra_in_tex:
            print(f"  [-] In Tex but not in PHP: {extra_in_tex}")
        if not extra_in_php and not extra_in_tex:
            print("  [OK] Methods match exactly!")
    else:
        print(f"\nClass {class_name} is missing in one of them.")
