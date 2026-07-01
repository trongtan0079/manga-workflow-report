# CHECKLIST CHI TIẾT — CHUẨN HÓA BÁO CÁO MANGA WORKFLOW

Bảng checklist này chứa tất cả các đầu việc cần làm để chuẩn hóa tài liệu báo cáo đồ án Manga Workflow theo mẫu của giảng viên, phân công chi tiết theo 4 Phase triển khai và các thành viên phụ trách.

---

## 📅 PHASE 1: KHÓA CẤU TRÚC & DỌN DẸP HỆ THỐNG
*Mục tiêu: Thiết lập khung sườn thư mục LaTeX mới, dọn dẹp các lỗi cấu trúc hiện có trước khi di chuyển nội dung.*

### 🛠️ Việc cấu trúc & Cấu hình (Trương Trọng Tấn)
- [x] **[P1-01]** Tạo các file `.tex` mới với cấu trúc rỗng (chỉ có lệnh `\chapter`, `\section`, `\label`).
- [x] **[P1-02]** Cập nhật file `main.tex` để import đúng thứ tự các chương con thông qua lệnh `\input`.
- [x] **[P1-03]** Sửa lỗi trùng lặp nghiêm trọng trong file `chapters/03_3_uml_thiet_ke.tex` (xóa đoạn code bị lặp ở dòng 68-134).
- [x] **[P1-04]** Dọn dẹp tài nguyên thừa: Xóa file hình ảnh `Class_Diagram_pt.pdf` bị trùng lặp với `Class_Diagram.pdf`.
- [x] **[P1-05]** Chuẩn hóa lại định dạng bảng thuật ngữ trong `sections/thuat_ngu.tex`.
- [x] **[P1-06]** Build thử nghiệm PDF của khung sườn mới để đảm bảo không gặp lỗi biên dịch (compile error).

---

## 📦 PHASE 2: DI CHUYỂN NỘI DUNG CŨ
*Mục tiêu: Đưa toàn bộ nội dung từ các file cũ vào đúng vị trí mới trong cây thư mục.*

### 🔄 Di chuyển nội dung SRS (Giang Thị Ngọc Hân & Nguyễn Thanh Thảo)
- [ ] **[P2-01]** Chuyển phần Giới thiệu chung & Quy trình nghiệp vụ từ `02_1_yeu_cau_chuc_nang.tex` sang `03_1_srs_tong_quan.tex`.
- [ ] **[P2-02]** Chuyển bảng mô tả Actor từ `03_2_uml_nghiep_vu.tex` và phần mô tả actor từ `01_gioi_thieu.tex` gộp chung vào `03_1_srs_tong_quan.tex` (§3.2.1).
- [ ] **[P2-03]** Di chuyển các sơ đồ Use Case (Admin, Mangaka, Assistant, Tantou Editor, Editorial Board) từ `03_2` sang `03_1_srs_tong_quan.tex` (§3.2.2).
- [x] **[P2-04]** Di chuyển nội dung phần Yêu cầu phi chức năng (NFR) từ `02_2_yeu_cau_phi_chuc_nang.tex` sang `03_4_srs_nfr.tex`.

### 🔄 Di chuyển nội dung SDD (Nguyễn Thị Trúc Ngân & Phan Thị Hạnh)
- [ ] **[P2-05]** Di chuyển thiết kế kiến trúc hệ thống và deployment từ `03_1_thiet_ke_tong_the.tex` sang `04_1_sdd_system.tex`.
- [ ] **[P2-06]** Di chuyển sơ đồ Swimlane và 3 sơ đồ Activity từ `03_2_uml_nghiep_vu.tex` sang `04_3_sdd_detailed.tex` (§4.3.1).
- [ ] **[P2-07]** Di chuyển 5 sơ đồ Sequence Diagram (đã dọn dẹp phần trùng lặp) từ `03_3_uml_thiet_ke.tex` sang `04_3_sdd_detailed.tex` (§4.3.2).
- [ ] **[P2-08]** Di chuyển Class Diagram tổng thể và mô tả các lớp từ `03_3` sang `04_3_sdd_detailed.tex` (§4.3.3).
- [ ] **[P2-09]** Di chuyển Sơ đồ ERD, Data Dictionary (10 bảng) và mô tả mối quan hệ từ `03_4_database_ui.tex` sang `04_2_sdd_database.tex`.
- [ ] **[P2-10]** Di chuyển danh sách UI hiện tại từ `03_4` sang `04_4_sdd_ui.tex`.

### 🔄 Đồng bộ hóa tham chiếu (Cả nhóm thực hiện phần mình phụ trách)
- [ ] **[P2-11]** Sửa lại toàn bộ các nhãn `\label` bị trùng hoặc bị lỗi do phân tách file.
- [ ] **[P2-12]** Cập nhật lại đường dẫn hình ảnh trong lệnh `\includegraphics` tương ứng với vị trí file mới.
- [ ] **[P2-13]** Sửa lại các liên kết chéo `\ref` và `\pageref` trong tài liệu.

---

## ✍️ PHASE 3: VIẾT MỚI & HOÀN THIỆN NỘI DUNG THIẾU
*Mục tiêu: Triển khai viết mới các chương, các sơ đồ UML và chi tiết kịch bản sử dụng còn thiếu.*

### ✍️ Chương I: Giới thiệu dự án (Trương Trọng Tấn)
- [ ] **[P3-01]** Viết mục **1.3 Hệ thống hiện có** (§1.3.1 Quản lý thủ công, §1.3.2 Công cụ Trello/Notion và nhược điểm).
- [ ] **[P3-02]** Viết mục **1.4 Cơ hội phát triển** (Lý do xây dựng, cơ hội tối ưu quy trình manga).
- [ ] **[P3-03]** Xem xét loại bỏ phần Kết luận chương ở cuối Chương 1 theo đúng mẫu.

### ✍️ Chương II: Kế hoạch quản lý dự án - SPMP (Nguyễn Thị Trúc Ngân)
- [ ] **[P3-04]** Lập bảng phân tích **WBS (Work Breakdown Structure)** và ước lượng công sức (Man-days).
- [ ] **[P3-05]** Viết mục **2.1.2 Mục tiêu dự án** (chỉ tiêu thời gian, nỗ lực) và **2.1.3 Rủi ro dự án** (bảng Risk + kế hoạch ứng phó).
- [ ] **[P3-06]** Mô tả **Quy trình phát triển phần mềm** áp dụng và phương pháp quản lý chất lượng.
- [ ] **[P3-07]** Bổ sung **Sản phẩm bàn giao** theo từng giai đoạn / Sprint.
- [ ] **[P3-08]** Xây dựng ma trận phân công trách nhiệm **RACI**.
- [ ] **[P3-09]** Viết các phần Giao tiếp dự án & Quản lý cấu hình (tài liệu, mã nguồn, hạ tầng).

### ✍️ Chương III: Đặc tả yêu cầu phần mềm - SRS
#### Phần tổng quan & UC Spec 1 (Giang Thị Ngọc Hân)
- [ ] **[P3-10]** Vẽ sơ đồ ngữ cảnh **Context Diagram** (§3.1.2) cho hệ thống Manga Workflow.
- [ ] **[P3-11]** Lập **Bảng tóm tắt Use Case** (§3.2.3) gồm cột ID, Use Case, Actor, Mô tả ngắn.
- [ ] **[P3-12]** Viết phần **System Functional Overview** (§3.3.1) gồm: Screens Flow, Screen Descriptions, Screen Authorization (ma trận Actor-Screen).
- [ ] **[P3-13]** Đặc tả chi tiết Use Case (UC Spec) cho các module:
  - [ ] UC-01 Đăng nhập & UC-02 Đăng xuất.
  - [ ] UC-03 đến UC-06 (Quản lý người dùng: Xem, Tạo, Cập nhật, Khóa).
  - [ ] UC-07 đến UC-10 (Quản lý Series: Tạo, Xem, Cập nhật, Theo dõi trạng thái).

#### Phần UC Spec 2 (Nguyễn Thanh Thảo)
- [ ] **[P3-14]** Đặc tả chi tiết Use Case (UC Spec) cho các module:
  - [ ] UC-11 đến UC-13 (Quản lý Chapter: Tạo, Cập nhật, Theo dõi).
  - [ ] UC-14 đến UC-15 (Quản lý Page: Tạo, Cập nhật trạng thái).
  - [ ] UC-16 đến UC-19 (Quản lý Task: Tạo/Phân công, Cập nhật, Theo dõi, Hủy).
  - [ ] UC-20 đến UC-22 (Quản lý Submission: Nộp, Xem chi tiết, Lịch sử).
  - [ ] UC-23 đến UC-25 (Quản lý Review: Tạo, Xem chi tiết, Phản hồi sửa).
  - [ ] UC-26 đến UC-28 (Xét duyệt & Xuất bản: Duyệt Series, Xuất bản Chapter, Ngừng phát hành).
  - [ ] UC-29 đến UC-31 (Quản lý Xếp hạng: Nhập vote, Xem BXH, Xem lịch sử).
  - [ ] UC-32 đến UC-33 (Quản lý Thông báo: Xem, Đánh dấu đã đọc).

#### Phần NFR & Quy tắc nghiệp vụ (Dương Kim Ngân)
- [ ] **[P3-15]** Chuẩn hóa NFR: Thêm các chỉ số đo lường cụ thể cho Hiệu năng, Bảo mật, Khả năng mở rộng, Tính sẵn sàng, Khả năng sử dụng, Khả năng bảo trì.

### ✍️ Chương IV: Thiết kế hệ thống - SDD
#### Kiến trúc & Thiết kế chi tiết (Nguyễn Thị Trúc Ngân)
- [ ] **[P3-16]** Vẽ sơ đồ thành phần **Component / Package Diagram** (§4.1.3).
- [ ] **[P3-17]** Viết mô tả chi tiết công nghệ sử dụng (**Technology Stack**).
- [ ] **[P3-18]** Bổ sung danh sách các **phương thức (Methods)** cho từng thực thể trong Class Diagram.

#### Thiết kế giao diện (Phan Thị Hạnh)
- [ ] **[P3-19]** Thiết kế **UI Mockup/Wireframe** cho 9 giao diện chính:
  - [ ] Dashboard (chung và riêng theo vai trò)
  - [ ] Trang đăng nhập
  - [ ] Quản lý Series (Danh sách & Chi tiết)
  - [ ] Quản lý Chapter
  - [ ] Quản lý Task
  - [ ] Giao diện Nộp Submission
  - [ ] Giao diện Review & Đánh giá
  - [ ] Trung tâm thông báo
  - [ ] Bảng xếp hạng Series

### ✍️ Chương V: Tài liệu kiểm thử - Testing (Dương Kim Ngân)
- [ ] **[P3-20]** Xác định **Phạm vi kiểm thử** (§5.1).
- [ ] **[P3-21]** Xây dựng **Chiến lược kiểm thử** (§5.2) và **Kế hoạch kiểm thử** (§5.3).
- [ ] **[P3-22]** Triển khai viết chi tiết **15 kịch bản kiểm thử (Test Cases)** từ TC-01 đến TC-15.
- [ ] **[P3-23]** Thiết lập biểu mẫu **Báo cáo kiểm thử** (§5.5) thống kê kết quả Pass/Fail.

### ✍️ Chương VI: Gói phát hành & Hướng dẫn sử dụng (Phan Thị Hạnh)
- [ ] **[P3-24]** Lập danh mục gói sản phẩm bàn giao (Deliverable Package).
- [ ] **[P3-25]** Viết hướng dẫn cài đặt chi tiết (Yêu cầu hệ thống, cấu hình môi trường, setup database).
- [ ] **[P3-26]** Viết hướng dẫn sử dụng (User Manual) chi tiết cho cả 5 Actor.

### ✍️ Chương VII & Phụ lục (Trương Trọng Tấn)
- [ ] **[P3-27]** Viết phần **Kết luận & Hướng phát triển** ở chương cuối.
- [ ] **[P3-28]** Bổ sung tài liệu API trong Phụ lục A (ít nhất 5-10 endpoint thực tế).

---

## 🔍 PHASE 4: REVIEW & ĐỒNG BỘ FORMAT
*Mục tiêu: Đảm bảo toàn bộ tài liệu nhất quán về mặt trình bày và không có lỗi biên dịch.*

### 🔍 Kiểm tra & Đồng bộ hóa (Trương Trọng Tấn)
- [ ] **[P4-01]** Đồng bộ font chữ, khoảng cách dòng, lề trang theo cấu hình `config/`.
- [ ] **[P4-02]** Đồng bộ định dạng bảng biểu, tiêu đề hình vẽ và chú thích (caption).
- [ ] **[P4-03]** Kiểm tra lỗi chính tả tiếng Việt và thuật ngữ chuyên ngành toàn bộ báo cáo.
- [ ] **[P4-04]** Biên dịch thử nghiệm lần cuối, kiểm tra log cảnh báo (warning) và sửa triệt để.
- [ ] **[P4-05]** Xuất bản bản in PDF chính thức để nộp giảng viên.
