import shutil
import os

source_dir = r"d:\LapTrinhWeb\manga-workflow-report\Manga-publishing-management-system\UML"
target_dir = r"d:\LapTrinhWeb\manga-workflow-report\UML"

files_to_copy = [
    "Activity_Diagram_Quy_Trình_Giao_Và_Thực_Hiện_Task.puml",
    "Activity_Diagram_quy trình_Review_Chapter.puml",
    "Activity_Diagram_quy_trình_xuất_bản_Manga.puml",
    "Class_Diagram.puml",
    "Deployment_Diagram.puml",
    "ERD.puml",
    "State_Machine_Chapter.puml",
    "State_Machine_Page.puml",
    "State_Machine_Page_Region.puml",
    "State_Machine_Series.puml",
    "State_Machine_Task.puml",
    "Swimlane_tong_quat_quy_trinh_sang_tac_maga.puml",
    "System_Architecture_Diagram.puml",
    "Use_Case_Diagram.puml",
    "sequence_diagram_dang_nhap_he_thong.puml",
    "sequence_diagram_manga_series_publishing.puml",
    "sequence_diagram_manga_task_assignment.puml",
    "sequence_diagram_quy_trinh_nop_submission.puml",
    "sequence_diagram_review_chapter.puml"
]

print("Syncing PUML files from code to report:")
for filename in files_to_copy:
    src_path = os.path.join(source_dir, filename)
    dst_path = os.path.join(target_dir, filename)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        try:
            print("Copied: " + filename.encode('ascii', errors='replace').decode('ascii'))
        except Exception:
            print("Copied a file.")
    else:
        print("Warning: Source file does not exist.")
print("Done!")
