import zlib
import base64
import urllib.request
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def plantuml_encode(puml_text):
    zlibbed_str = zlib.compress(puml_text.encode('utf-8'))
    compressed_string = zlibbed_str[2:-4]
    mapping = bytes.maketrans(
        b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/',
        b'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'
    )
    return base64.b64encode(compressed_string).translate(mapping).decode('ascii')

def compile_puml_to_png(puml_path, output_png_path):
    print(f"Reading {puml_path}...")
    with open(puml_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    encoded = plantuml_encode(text)
    # Try multiple servers
    servers = [
        f"http://www.plantuml.com/plantuml/png/{encoded}",
        f"https://kroki.io/plantuml/png/{encoded}",
    ]
    
    for url in servers:
        print(f"Trying: {url[:80]}...")
        try:
            req = urllib.request.Request(
                url, 
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                    'Accept': 'image/png,image/*,*/*',
                    'Accept-Language': 'en-US,en;q=0.9',
                }
            )
            with urllib.request.urlopen(req, timeout=30) as response:
                content = response.read()
                if len(content) > 1000:  # valid PNG
                    os.makedirs(os.path.dirname(output_png_path), exist_ok=True)
                    with open(output_png_path, 'wb') as out_f:
                        out_f.write(content)
                    print(f"Saved to {output_png_path} successfully! ({len(content)} bytes)")
                    return
                else:
                    print(f"Response too small ({len(content)} bytes), trying next server...")
        except Exception as e:
            print(f"Failed with {url[:60]}: {e}")
    
    print(f"ERROR: All servers failed for {puml_path}")

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Only compile State_Machine_Page.puml (single file mode)
    if len(sys.argv) > 1:
        puml_rel = sys.argv[1]
        png_rel = sys.argv[2]
        compile_puml_to_png(
            os.path.join(base_dir, puml_rel),
            os.path.join(base_dir, png_rel)
        )
        return
    
    mapping = {
        "UML/Activity_Diagram_Quy_Trình_Giao_Và_Thực_Hiện_Task.puml": "assets/diagrams/Chapter3_IMAGE/Activity_Diagram_quy_trinh_giao_va_thuc_hien_Task.png",
        "UML/Activity_Diagram_quy trình_Review_Chapter.puml": "assets/diagrams/Chapter3_IMAGE/Activity_Diagram_quy_trinh_Review_Chapter.png",
        "UML/Activity_Diagram_quy_trình_xuất_bản_Manga.puml": "assets/diagrams/Chapter3_IMAGE/Activity_Diagram_quy_trinh_xuat_ban_Manga.png",
        "UML/Context_Diagram.puml": "assets/diagrams/Chapter3_IMAGE/Context_Diagram.png",
        "UML/ERD.puml": "assets/diagrams/Chapter3_IMAGE/ERD.png",
        "UML/Class_Diagram.puml": "assets/diagrams/Chapter3_IMAGE/class_diagram.png",
        "UML/Deployment_Diagram.puml": "assets/diagrams/Chapter3_IMAGE/kien_truc_trien_khai_he_thong.png",
        "UML/State_Machine_Page.puml": "assets/diagrams/Chapter3_IMAGE/State_Machine_Page.png",
        "UML/State_Machine_Chapter.puml": "assets/diagrams/Chapter3_IMAGE/State_Machine_Chapter.png",
        "UML/State_Machine_Page_Region.puml": "assets/diagrams/Chapter3_IMAGE/State_Machine_Page_Region.png",
        "UML/State_Machine_Series.puml": "assets/diagrams/Chapter3_IMAGE/State_Machine_Series.png",
        "UML/State_Machine_Task.puml": "assets/diagrams/Chapter3_IMAGE/State_Machine_Task.png",
        "UML/Swimlane_tong_quat_quy_trinh_sang_tac_maga.puml": "assets/diagrams/Chapter3_IMAGE/Swimlane_tong_quat_quy_trinh_sang_tac_maga.png",
        "UML/Use_Case_Diagram.puml": "assets/diagrams/Chapter3_IMAGE/Use_case_tong_quat.png",
        "UML/System_Architecture_Diagram.puml": "assets/diagrams/Chapter3_IMAGE/System_Architecture_Diagram.png",
        "UML/sequence_diagram_dang_nhap_he_thong.puml": "assets/diagrams/Chapter3_IMAGE/sequence_diagram_dang_nhap_he_thong.png",
        "UML/sequence_diagram_manga_task_assignment.puml": "assets/diagrams/Chapter3_IMAGE/sequence_diagram_manga_task_assignment.png",
        "UML/sequence_diagram_quy_trinh_nop_submission.puml": "assets/diagrams/Chapter3_IMAGE/sequence_diagram_quy_trinh_nop_submission.png",
        "UML/sequence_diagram_review_chapter.puml": "assets/diagrams/Chapter3_IMAGE/sequence_diagram_review_chapter.png",
        "UML/sequence_diagram_manga_series_publishing.puml": "assets/diagrams/Chapter3_IMAGE/sequence_diagram_manga_series_publishing.png",
    }
    
    for puml_rel, png_rel in mapping.items():
        puml_path = os.path.join(base_dir, puml_rel)
        png_path = os.path.join(base_dir, png_rel)
        compile_puml_to_png(puml_path, png_path)

if __name__ == "__main__":
    main()
