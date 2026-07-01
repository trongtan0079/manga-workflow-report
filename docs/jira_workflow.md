# 📊 BẢNG THEO DÕI CÔNG VIỆC JIRA (JIRA WORKFLOW & CHECKLIST)
## Manga Creation Workflow and Publishing Management System

> [!NOTE]  
> Tài liệu này ghi nhận toàn bộ lịch sử các công việc đã hoàn thành (của cuốn báo cáo cũ và Phase 1) cùng danh sách các Task chi tiết cần phân công trên Jira cho các thành viên trong các Phase tiếp theo.

---

## 👑 1. TRƯƠNG TRỌNG TẤN (Leader)

### ✅ Công việc đã hoàn thành
- [x] **[OLD-01]** Soạn thảo Lời cảm ơn, bảng Thuật ngữ và từ viết tắt.
- [x] **[OLD-02]** Soạn thảo Chương I: Giới thiệu dự án (Bản thảo cũ).
- [x] **[P1-01]** Tạo các file `.tex` mới với cấu trúc rỗng trong thư mục LaTeX mới.
- [x] **[P1-02]** Cập nhật file `main.tex` để import đúng thứ tự các chương con thông qua lệnh `\input`.
- [x] **[P1-03]** Sửa lỗi trùng lặp nghiêm trọng trong file `chapters/03_3_uml_thiet_ke.tex` (xóa đoạn code bị lặp ở dòng 68-134).
- [x] **[P1-04]** Dọn dẹp tài nguyên thừa: Xóa file hình ảnh `Class_Diagram_pt.pdf` bị trùng lặp.
- [x] **[P1-05]** Chuẩn hóa lại định dạng bảng thuật ngữ trong `sections/thuat_ngu.tex`.
- [x] **[P1-06]** Biên dịch (compile) thử nghiệm PDF của khung sườn mới thành công không lỗi.
- [x] **[P3-01/02/03]** Soạn thảo bổ sung nội dung Chương I (Hệ thống hiện có, cơ hội phát triển, loại bỏ phần kết luận).

### 📋 Task phân công Jira tiếp theo
- [ ] **[Phase 3 - Tấn]** Soạn thảo Chương VII & Phụ lục:
  * Viết phần **Kết luận & Hướng phát triển** ở chương cuối (`chapters/07_ket_luan.tex`).
  * Soạn thảo tài liệu API trong Phụ lục A (mô tả ít nhất 5-10 endpoint thực tế).
- [ ] **[Phase 4 - Tấn]** Chuẩn hóa định dạng và nghiệm thu tài liệu LaTeX:
  * Đồng bộ font chữ, khoảng cách dòng, lề trang theo cấu hình.
  * Đồng bộ định dạng bảng biểu, caption hình vẽ.
  * Kiểm tra lỗi chính tả tiếng Việt và thuật ngữ.
  * Biên dịch thử nghiệm lần cuối, kiểm tra log cảnh báo (warning) và sửa triệt để.
  * Xuất bản bản in PDF chính thức nộp giảng viên.

---

## 📝 2. GIANG THỊ NGỌC HÂN

### ✅ Công việc đã hoàn thành
- [x] **[OLD-03]** Đưa nội dung phân tích yêu cầu chức năng vào LaTeX (Chương II bản cũ).
- [x] **[OLD-04]** Đưa nội dung thu thập và phân tích yêu cầu từ người dùng vào LaTeX.
- [x] **[OLD-05]** Đưa nội dung mô tả chi tiết vai trò và chức năng của từng Actor vào LaTeX.

### 📋 Task phân công Jira tiếp theo
- [ ] **[Phase 2 - Hân]** Di chuyển và gộp nội dung SRS (Mô tả & Actors):
  * Di chuyển phần Giới thiệu chung & Quy trình nghiệp vụ từ `02_1_yeu_cau_chuc_nang.tex` sang `03_1_srs_tong_quan.tex`.
  * Di chuyển bảng mô tả Actor từ `03_2_uml_nghiep_vu.tex` và phần mô tả actor từ `01_gioi_thieu.tex` gộp chung vào `03_1_srs_tong_quan.tex` (§3.2.1).
  * Di chuyển các sơ đồ Use Case (Admin, Mangaka, Assistant, Tantou Editor, Editorial Board) từ `03_2` sang `03_1_srs_tong_quan.tex` (§3.2.2).
- [ ] **[Phase 3 - Hân]** Vẽ sơ đồ và đặc tả Use Case Module 1:
  * Vẽ sơ đồ ngữ cảnh **Context Diagram** (§3.1.2) cho hệ thống Manga Workflow.
  * Lập **Bảng tóm tắt Use Case** (§3.2.3) gồm cột ID, Use Case, Actor, Mô tả ngắn.
  * Viết phần **System Functional Overview** (§3.3.1) gồm: Screens Flow, Screen Descriptions, Screen Authorization (ma trận Actor-Screen).
  * Đặc tả chi tiết Use Case (UC Spec) cho các module:
    * UC-01 Đăng nhập & UC-02 Đăng xuất.
    * UC-03 đến UC-06 (Quản lý người dùng: Xem, Tạo, Cập nhật, Khóa).
    * UC-07 đến UC-10 (Quản lý Series: Tạo, Xem, Cập nhật, Theo dõi trạng thái).

---

## 🎨 3. NGUYỄN THANH THẢO

### ✅ Công việc đã hoàn thành
- [x] **[OLD-06]** Đưa sơ đồ Use Case Diagram tổng thể và chi tiết vào LaTeX.
- [x] **[OLD-07]** Đưa sơ đồ Swimlane Diagram và Activity Diagram cho các quy trình nghiệp vụ vào LaTeX.
- [x] **[OLD-08]** Đưa mô tả nghiệp vụ chi tiết cho từng sơ đồ vào LaTeX.

### 📋 Task phân công Jira tiếp theo
- [ ] **[Phase 2 - Thảo]** Di chuyển nội dung SRS (Yêu cầu phi chức năng NFR):
  * Di chuyển nội dung phần Yêu cầu phi chức năng (NFR) từ `02_2_yeu_cau_phi_chuc_nang.tex` sang `03_4_srs_nfr.tex`.
- [ ] **[Phase 3 - Thảo]** Đặc tả chi tiết Use Case Module 2:
  * Đặc tả chi tiết Use Case (UC Spec) cho các module còn lại trong file `chapters/03_3_srs_func_2.tex`:
    * UC-11 đến UC-13 (Quản lý Chapter: Tạo, Cập nhật, Theo dõi).
    * UC-14 đến UC-15 (Quản lý Page: Tạo, Cập nhật trạng thái).
    * UC-16 đến UC-19 (Quản lý Task: Tạo/Phân công, Cập nhật, Theo dõi, Hủy).
    * UC-20 đến UC-22 (Quản lý Submission: Nộp, Xem chi tiết, Lịch sử).
    * UC-23 đến UC-25 (Quản lý Review: Tạo, Xem chi tiết, Phản hồi sửa).
    * UC-26 đến UC-28 (Xét duyệt & Xuất bản: Duyệt Series, Xuất bản Chapter, Ngừng phát hành).
    * UC-29 đến UC-31 (Quản lý Xếp hạng: Nhập vote, Xem BXH, Xem lịch sử).
    * UC-32 đến UC-33 (Quản lý Thông báo: Xem, Đánh dấu đã đọc).

---

## 📐 4. NGUYỄN THỊ TRÚC NGÂN

### ✅ Công việc đã hoàn thành
- [x] **[OLD-09]** Đưa nội dung mô tả kiến trúc tổng thể và sơ đồ triển khai của hệ thống vào LaTeX.
- [x] **[OLD-10]** Đưa sơ đồ Sequence Diagram cho các luồng xử lý chính vào LaTeX.
- [x] **[OLD-11]** Đưa sơ đồ Class Diagram chi tiết của hệ thống (Sơ đồ do cả nhóm cùng vẽ) vào LaTeX.

### 📋 Task phân công Jira tiếp theo
- [ ] **[Phase 2 - Trúc Ngân]** Di chuyển nội dung SDD (Kiến trúc & Class Diagram):
  * Di chuyển thiết kế kiến trúc hệ thống và deployment từ `03_1_thiet_ke_tong_the.tex` sang `04_1_sdd_system.tex`.
  * Di chuyển Class Diagram tổng thể và mô tả các lớp từ `03_3` sang `04_3_sdd_detailed.tex` (§4.3.3).
- [ ] **[Phase 3 - Trúc Ngân]** Soạn thảo Chương II (Kế hoạch quản lý dự án SPMP) & UML bổ sung:
  * Lập bảng phân tích **WBS (Work Breakdown Structure)** và ước lượng công sức (Man-days).
  * Viết mục **2.1.2 Mục tiêu dự án** (chỉ tiêu thời gian, nỗ lực) và **2.1.3 Rủi ro dự án** (bảng Risk + kế hoạch ứng phó).
  * Mô tả **Quy trình phát triển phần mềm** áp dụng và phương pháp quản lý chất lượng.
  * Bổ sung **Sản phẩm bàn giao** theo từng giai đoạn / Sprint.
  * Xây dựng ma trận phân công trách nhiệm **RACI**.
  * Viết các phần Giao tiếp dự án & Quản lý cấu hình (tài liệu, mã nguồn, hạ tầng).
  * Vẽ sơ đồ thành phần **Component / Package Diagram** (§4.1.3).
  * Viết mô tả chi tiết công nghệ sử dụng (**Technology Stack**).
  * Bổ sung danh sách các **phương thức (Methods)** cho từng thực thể trong Class Diagram.

---

## 💾 5. PHAN THỊ HẠNH

### ✅ Công việc đã hoàn thành
- [x] **[OLD-12]** Đưa lược đồ cơ sở dữ liệu hệ thống (Database Schema) vào LaTeX.
- [x] **[OLD-13]** Đưa sơ đồ quan hệ thực thể (ERD - Sơ đồ do cả nhóm cùng vẽ) vào LaTeX.
- [x] **[OLD-14]** Đưa danh sách Từ điển dữ liệu (Data Dictionary) chi tiết cho các bảng vào LaTeX.

### 📋 Task phân công Jira tiếp theo
- [ ] **[Phase 2 - Hạnh]** Di chuyển nội dung SDD (CSDL & UML hành vi):
  * Di chuyển sơ đồ Swimlane và 3 sơ đồ Activity từ `03_2_uml_nghiep_vu.tex` sang `04_3_sdd_detailed.tex` (§4.3.1).
  * Di chuyển 5 sơ đồ Sequence Diagram (đã dọn dẹp phần trùng lặp) từ `03_3_uml_thiet_ke.tex` sang `04_3_sdd_detailed.tex` (§4.3.2).
  * Di chuyển Sơ đồ ERD, Data Dictionary (10 bảng) và mô tả mối quan hệ từ `03_4_database_ui.tex` sang `04_2_sdd_database.tex`.
  * Di chuyển danh sách UI hiện tại từ `03_4` sang `04_4_sdd_ui.tex`.
- [ ] **[Phase 3 - Hạnh]** Thiết kế UI Mockup & Hướng dẫn sử dụng:
  * Thiết kế **UI Mockup/Wireframe** cho 9 giao diện chính: Dashboard (chung & riêng), Trang đăng nhập, Quản lý Series (Danh sách & Chi tiết), Quản lý Chapter, Quản lý Task, Giao diện Nộp Submission, Giao diện Review & Đánh giá, Trung tâm thông báo, Bảng xếp hạng Series.
  * Lập danh mục gói sản phẩm bàn giao (Deliverable Package) trong `06_release.tex`.
  * Viết hướng dẫn cài đặt chi tiết (Yêu cầu hệ thống, cấu hình môi trường, setup database).
  * Viết hướng dẫn sử dụng (User Manual) chi tiết cho cả 5 Actor.

---

## 🔍 6. DƯƠNG KIM NGÂN

### ✅ Công việc đã hoàn thành
- [x] **[OLD-15]** Đưa nội dung phân tích các yêu cầu phi chức năng (NFR) vào LaTeX.
- [x] **[OLD-16]** Đưa nội dung các quy tắc nghiệp vụ hệ thống (Business Rules) vào LaTeX.
- [x] **[OLD-17]** Đưa các ràng buộc kỹ thuật và vận hành của hệ thống vào LaTeX.

### 📋 Task phân công Jira tiếp theo
- [ ] **[Phase 3 - Kim Ngân]** Chuẩn hóa NFR & Soạn thảo nội dung kiểm thử:
  * Chuẩn hóa NFR: Thêm các chỉ số đo lường cụ thể cho Hiệu năng, Bảo mật, Khả năng mở rộng, Tính sẵn sàng, Khả năng sử dụng, Khả năng bảo trì vào `03_4_srs_nfr.tex`.
  * Biên soạn Chương V (`chapters/05_kiem_thu.tex`): Xác định **Phạm vi kiểm thử**, **Chiến lược kiểm thử** và **Kế hoạch kiểm thử**.
  * Triển khai viết chi tiết **15 kịch bản kiểm thử (Test Cases)** từ TC-01 đến TC-15.
  * Thiết lập biểu mẫu **Báo cáo kiểm thử** thống kê kết quả Pass/Fail.

---

## 🔄 7. ĐỒNG BỘ THAM CHIẾU (Cả nhóm tự thực hiện trên file mình đảm nhận)
- [ ] **[Phase 2 - Cả nhóm]** Sửa lại toàn bộ các nhãn `\label` bị trùng hoặc bị lỗi do phân tách file.
- [ ] **[Phase 2 - Cả nhóm]** Cập nhật lại đường dẫn hình ảnh trong lệnh `\includegraphics` tương ứng với vị trí file mới.
- [ ] **[Phase 2 - Cả nhóm]** Sửa lại các liên kết chéo `\ref` và `\pageref` trong tài liệu.
