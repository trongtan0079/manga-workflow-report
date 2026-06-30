# 📋 KẾ HOẠCH THỰC HIỆN DỰ ÁN BAN ĐẦU (ORIGINAL PROJECT PLAN)
## Manga Creation Workflow and Publishing Management System

> [!NOTE]  
> Đây là tài liệu kế hoạch ban đầu của nhóm phục vụ cho quá trình phân tích và soạn thảo nội dung báo cáo (trước khi chuyển sang giai đoạn tái cấu trúc và chuẩn hóa SRS/SDD). 

---

## 🎯 1. Mục tiêu thực hiện
* **Đúng tiến độ:** Hoàn thành toàn bộ các giai đoạn của đồ án đúng thời gian quy định.
* **Chất lượng cao:** Đảm bảo nội dung báo cáo đầy đủ, chính xác, lập luận khoa học và thống nhất.
* **Phân vai rõ ràng:** Phân chia công việc hợp lý, phát huy tối đa năng lực cá nhân của từng thành viên.
* **Quản lý chuyên nghiệp:** Giám sát tiến độ chặt chẽ qua các công cụ hỗ trợ quản lý công việc hiện đại.
* **Đồng bộ dữ liệu:** Đảm bảo tính nhất quán tuyệt đối giữa tài liệu đặc tả thiết kế, sơ đồ UML và hệ thống thực tế.

---

## 👥 2. Phân chia công việc chi tiết (Phiên bản biên soạn nội dung)

Dưới đây là phân công nhiệm vụ đưa nội dung và biên soạn báo cáo LaTeX cho các thành viên:

### 👑 2.1. Trương Trọng Tấn (Leader)
* **Vai trò:** Tổng hợp & Quản lý dự án (Chuẩn bị mẫu nội dung báo cáo cho cả nhóm)
* **File LaTeX đảm nhận:** `01_gioi_thieu.tex`
* **Danh sách công việc:**
  * [x] Viết Lời cảm ơn, Thuật ngữ và từ viết tắt.
  * [x] Soạn thảo **Chương I: Giới thiệu dự án**.
  * [ ] Tổng hợp toàn bộ nội dung báo cáo đồ án.
  * [ ] Kiểm tra định dạng (format) tài liệu LaTeX.
  * [x] Quản lý GitHub Repository (Kiểm soát lỗi trình bày, duyệt và merge code/tài liệu).
  * [ ] Đảm bảo tính đồng bộ nội dung giữa các chương.

### 📝 2.2 Giang Thị Ngọc Hân
* **Vai trò:** Đưa nội dung yêu cầu chức năng vào tài liệu
* **File LaTeX đảm nhận:** `02_1_yeu_cau_chuc_nang.tex`
* **Danh sách công việc:**
  * [x] Soạn thảo và đưa nội dung **Chương II: Tổng quan hệ thống** vào LaTeX.
  * [x] Đưa nội dung phân tích yêu cầu từ phía người dùng vào LaTeX.
  * [x] Đưa nội dung đặc tả yêu cầu chức năng vào LaTeX.
  * [x] Đưa nội dung mô tả chi tiết vai trò và chức năng của từng Actor vào LaTeX.
  * [x] Hoàn thiện tài liệu đặc tả chức năng hệ thống trên LaTeX.

### 🔍 2.3. Dương Kim Ngân
* **Vai trò:** Đưa nội dung yêu cầu phi chức năng & Nghiệp vụ vào tài liệu
* **File LaTeX đảm nhận:** `02_2_yeu_cau_phi_chuc_nang.tex`
* **Danh sách công việc:**
  * [x] Đưa nội dung phân tích các yêu cầu phi chức năng vào LaTeX.
  * [x] Đưa nội dung các quy tắc nghiệp vụ hệ thống (Business Rules) vào LaTeX.
  * [x] Đưa các ràng buộc kỹ thuật và vận hành của hệ thống vào LaTeX.
  * [x] Đưa phần giả định hệ thống vào LaTeX.
  * [x] Viết phần kết luận cho Chương II.

### 🎨 2.4. Nguyễn Thanh Thảo
* **Vai trò:** Đưa nội dung Use Case & Quy trình nghiệp vụ vào tài liệu
* **File LaTeX đảm nhận:** `03_2_uml_nghiep_vu.tex`
* **Danh sách công việc:**
  * [x] Đưa danh sách và mô tả các Actor vào LaTeX.
  * [x] Đưa sơ đồ Use Case Diagram tổng thể và chi tiết vào LaTeX.
  * [x] Đưa sơ đồ Swimlane Diagram và Activity Diagram cho các quy trình nghiệp vụ vào LaTeX.
  * [x] Đưa mô tả nghiệp vụ chi tiết cho từng sơ đồ vào LaTeX.

### 📐 2.5. Nguyễn Thị Trúc Ngân
* **Vai trò:** Đưa nội dung Kiến trúc & UML hệ thống vào tài liệu
* **File LaTeX đảm nhận:** `03_1_thiet_ke_tong_the.tex` và `03_3_uml_thiet_ke.tex`
* **Danh sách công việc:**
  * [x] Đưa nội dung mô tả kiến trúc tổng thể của hệ thống vào LaTeX.
  * [x] Đưa sơ đồ triển khai hệ thống (Deployment Diagram) vào LaTeX.
  * [x] Đưa sơ đồ Sequence Diagram cho các luồng xử lý chính vào LaTeX.
  * [x] Đưa sơ đồ Class Diagram chi tiết của hệ thống (Sơ đồ do cả nhóm cùng vẽ) vào LaTeX.
  * [x] Đưa mô tả cấu trúc các lớp chính và mối quan hệ giữa các lớp vào LaTeX.

### 💾 2.6. Phan Thị Hạnh
* **Vai trò:** Đưa nội dung Cơ sở dữ liệu (Database) vào tài liệu
* **File LaTeX đảm nhận:** `03_4_database_ui.tex`
* **Danh sách công việc:**
  * [x] Đưa nội dung lược đồ cơ sở dữ liệu hệ thống (Database Schema) vào LaTeX.
  * [x] Đưa sơ đồ quan hệ thực thể (ERD) vào tài liệu (Sơ đồ do cả nhóm cùng vẽ).
  * [x] Đưa nội dung Từ điển dữ liệu (Data Dictionary) chi tiết cho các bảng vào LaTeX.
  * [x] Đưa nội dung định nghĩa các thuộc tính, khóa chính, khóa ngoại và ràng buộc dữ liệu vào LaTeX.
  * [x] Kiểm tra và tối ưu hóa tính toàn vẹn dữ liệu trên LaTeX.
