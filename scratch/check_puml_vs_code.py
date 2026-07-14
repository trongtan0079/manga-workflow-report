import os
import re

models_dir = r"d:\LapTrinhWeb\manga-workflow-report\Manga-publishing-management-system\models"
puml_file = r"d:\LapTrinhWeb\manga-workflow-report\UML\Class_Diagram.puml"

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
                "methods": methods
            }

# 2. Parse PUML class diagram
puml_classes = {}
with open(puml_file, "r", encoding="utf-8") as f:
    puml_content = f.read()

# Match class definitions like: class Name { ... }
class_blocks = re.findall(r"class\s+(\w+)\s*\{(.*?)\}", puml_content, re.DOTALL)
for class_name, block_content in class_blocks:
    # Find methods: +methodName(param: type) : returnType
    methods = re.findall(r"\+\s*(\w+)\s*\((.*?)\)\s*:\s*(\w+)", block_content)
    puml_classes[class_name] = {
        "methods": methods
    }

# 3. Compare
print("=== COMPARING CLASSES ===")
php_classes = set(php_models.keys())
puml_class_names = set(puml_classes.keys())

missing_in_puml = php_classes - puml_class_names
missing_in_php = puml_class_names - php_classes

print(f"Classes in PHP: {php_classes}")
print(f"Classes in PUML: {puml_class_names}")
print(f"Missing in PUML: {missing_in_puml}")
print(f"Missing in PHP: {missing_in_php}")

print("\n=== COMPARING METHODS BY CLASS ===")
for class_name in sorted(php_classes.union(puml_class_names)):
    if class_name in php_models and class_name in puml_classes:
        php_methods = {m[0] for m in php_models[class_name]["methods"]}
        puml_methods = {m[0] for m in puml_classes[class_name]["methods"]}
        
        extra_in_php = php_methods - puml_methods
        extra_in_puml = puml_methods - php_methods
        
        print(f"\nClass {class_name}:")
        print(f"  PHP methods: {sorted(php_methods)}")
        print(f"  PUML methods: {sorted(puml_methods)}")
        if extra_in_php:
            print(f"  [+] In PHP but not in PUML: {extra_in_php}")
        if extra_in_puml:
            print(f"  [-] In PUML but not in PHP: {extra_in_puml}")
    else:
        print(f"\nClass {class_name} is missing in one of them.")
