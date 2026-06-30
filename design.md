# MỤC LỤC CHI TIẾT — Báo cáo đồ án Manga Workflow

> [!IMPORTANT]
> Đây là **cấu trúc mục lục** theo đúng mẫu SRS giảng viên. **Chưa viết nội dung, chưa sửa LaTeX.**
> Sau khi nhóm duyệt mục lục này → khóa cấu trúc → phân công viết từng section.

---

```
╔══════════════════════════════════════════════════════════════╗
║                     PHẦN MỞ ĐẦU                            ║
╚══════════════════════════════════════════════════════════════╝

Trang bìa                                                  (Existing)
Lời cảm ơn                                                 (Existing)
Tóm tắt đồ án                                              (Existing)
Danh mục thuật ngữ và viết tắt                              (Existing — cần bổ sung)
Mục lục                                                     (Existing)
Danh sách hình                                              (Existing)
Danh sách bảng                                              (Existing)


╔══════════════════════════════════════════════════════════════╗
║  I. GIỚI THIỆU DỰ ÁN (Project Introduction)               ║
╚══════════════════════════════════════════════════════════════╝

1.1 Tổng quan (Overview)
    1.1.1 Thông tin dự án                                   (Existing)
    1.1.2 Nhóm thực hiện                                    (Existing)

1.2 Bối cảnh sản phẩm (Product Background)
    1.2.1 Thực trạng hiện nay                               (Existing)
    1.2.2 Vấn đề cần giải quyết                             (Existing)

1.3 Hệ thống hiện có (Existing Systems)
    1.3.1 Phân tích hệ thống quản lý thủ công               (Need to Create)
    1.3.2 Phân tích hệ thống quản lý dự án phổ biến         (Need to Create)

1.4 Cơ hội phát triển (Business Opportunity)                (Need to Create)

1.5 Tầm nhìn sản phẩm (Software Product Vision)
    1.5.1 Mục tiêu hệ thống                                 (Existing)
    1.5.2 Giá trị mang lại                                   (Existing)

1.6 Phạm vi và giới hạn (Project Scope & Limitations)
    1.6.1 Chức năng chính (Major Features)
          Chức năng Admin                                    (Existing)
          Chức năng Mangaka                                  (Existing)
          Chức năng Assistant                                (Existing)
          Chức năng Tantou Editor                            (Existing)
          Chức năng Editorial Board                          (Existing)
    1.6.2 Giới hạn hệ thống (Limitations & Exclusions)      (Existing)
    1.6.3 Giả định và ràng buộc                              (Existing)


╔══════════════════════════════════════════════════════════════╗
║  II. KẾ HOẠCH QUẢN LÝ DỰ ÁN (Project Management Plan)    ║
╚══════════════════════════════════════════════════════════════╝

2.1 Tổng quan (Overview)
    2.1.1 Phạm vi và ước lượng (Scope & Estimation)          (Need to Create)
    2.1.2 Mục tiêu dự án (Project Objectives)                (Need to Create)
    2.1.3 Rủi ro dự án (Project Risks)                       (Need to Create)

2.2 Phương pháp quản lý (Management Approach)
    2.2.1 Quy trình phát triển phần mềm                      (Need to Create)
    2.2.2 Quản lý chất lượng (Quality Management)             (Need to Create)

2.3 Sản phẩm bàn giao (Project Deliverables)                 (Need to Create)

2.4 Phân công trách nhiệm (Responsibility Assignments)       (Need to Create)

2.5 Giao tiếp dự án (Project Communications)                  (Need to Create)

2.6 Quản lý cấu hình (Configuration Management)
    2.6.1 Quản lý tài liệu                                   (Need to Create)
    2.6.2 Quản lý mã nguồn                                   (Need to Create)
    2.6.3 Công cụ và hạ tầng                                  (Need to Create)


╔══════════════════════════════════════════════════════════════╗
║  III. ĐẶC TẢ YÊU CẦU PHẦN MỀM                            ║
║       (Software Requirement Specification)                  ║
╚══════════════════════════════════════════════════════════════╝

3.1 Tổng quan sản phẩm (Product Overview)
    3.1.1 Mô tả hệ thống (System Description)                (Existing)
    3.1.2 Sơ đồ ngữ cảnh (Context Diagram)                   (Need to Create)
    3.1.3 Quy trình nghiệp vụ tổng quát (Business Process)   (Existing)

3.2 Yêu cầu người dùng (User Requirements)
    3.2.1 Danh sách Actor (Actor List)                        (Need to Move — từ 03_2)
    3.2.2 Use Case Diagram
          Use Case Diagram tổng thể                          (Need to Move — từ 03_2)
          Use Case Diagram — Admin                           (Need to Move — từ 03_2)
          Use Case Diagram — Mangaka                         (Need to Move — từ 03_2)
          Use Case Diagram — Assistant                       (Need to Move — từ 03_2)
          Use Case Diagram — Tantou Editor                   (Need to Move — từ 03_2)
          Use Case Diagram — Editorial Board                 (Need to Move — từ 03_2)
    3.2.3 Bảng tóm tắt Use Case (Use Case Summary)           (Need to Create)
    3.2.4 Yêu cầu của từng nhóm người dùng
          Yêu cầu của Admin                                  (Existing)
          Yêu cầu của Mangaka                                (Existing)
          Yêu cầu của Assistant                              (Existing)
          Yêu cầu của Tantou Editor                          (Existing)
          Yêu cầu của Editorial Board                        (Existing)

3.3 Yêu cầu chức năng (Functional Requirements)
    3.3.1 Tổng quan chức năng (System Functional Overview)
          Screens Flow (Sơ đồ luồng màn hình)                (Need to Create)
          Screen Descriptions (Bảng mô tả màn hình)          (Need to Create)
          Screen Authorization (Ma trận phân quyền)           (Need to Create)
          Non-Screen Functions (Chức năng nền)                (Need to Create)

    3.3.2 Xác thực (Authentication)
          UC-01 Đăng nhập hệ thống                           (Need to Create)
          UC-02 Đăng xuất                                     (Need to Create)

    3.3.3 Quản lý người dùng (User Management)
          UC-03 Xem danh sách người dùng                     (Need to Create)
          UC-04 Tạo tài khoản                                (Need to Create)
          UC-05 Cập nhật thông tin người dùng                 (Need to Create)
          UC-06 Khóa / Mở khóa tài khoản                     (Need to Create)

    3.3.4 Quản lý Series (Manga Series Management)
          UC-07 Tạo hồ sơ Series mới                         (Need to Create)
          UC-08 Xem danh sách Series                          (Need to Create)
          UC-09 Cập nhật thông tin Series                     (Need to Create)
          UC-10 Theo dõi trạng thái Series                    (Need to Create)

    3.3.5 Quản lý Chapter (Chapter Management)
          UC-11 Tạo Chapter mới                               (Need to Create)
          UC-12 Cập nhật thông tin Chapter                    (Need to Create)
          UC-13 Theo dõi tiến độ Chapter                      (Need to Create)

    3.3.6 Quản lý Page (Page Management)
          UC-14 Tạo Page                                      (Need to Create)
          UC-15 Cập nhật trạng thái Page                      (Need to Create)

    3.3.7 Quản lý Task (Task Assignment & Tracking)
          UC-16 Tạo và phân công Task                         (Need to Create)
          UC-17 Cập nhật trạng thái Task                      (Need to Create)
          UC-18 Theo dõi tiến độ Task                         (Need to Create)
          UC-19 Hủy Task                                      (Need to Create)

    3.3.8 Quản lý Submission (Submission Management)
          UC-20 Nộp Submission                                (Need to Create)
          UC-21 Xem chi tiết Submission                       (Need to Create)
          UC-22 Xem lịch sử Submission                        (Need to Create)

    3.3.9 Quản lý Review (Review Management)
          UC-23 Tạo Review cho Submission                     (Need to Create)
          UC-24 Xem chi tiết Review                           (Need to Create)
          UC-25 Phản hồi yêu cầu chỉnh sửa                  (Need to Create)

    3.3.10 Xét duyệt & Xuất bản (Approval & Publishing)
           UC-26 Xét duyệt Series mới                        (Need to Create)
           UC-27 Xuất bản Chapter                             (Need to Create)
           UC-28 Quyết định ngừng phát hành                   (Need to Create)

    3.3.11 Quản lý Xếp hạng (Ranking Management)
           UC-29 Nhập dữ liệu bình chọn                     (Need to Create)
           UC-30 Xem bảng xếp hạng                            (Need to Create)
           UC-31 Xem lịch sử xếp hạng                        (Need to Create)

    3.3.12 Quản lý Thông báo (Notification Management)
           UC-32 Xem danh sách thông báo                     (Need to Create)
           UC-33 Đánh dấu đã đọc                             (Need to Create)

3.4 Yêu cầu phi chức năng (Non-Functional Requirements)
    3.4.1 Hiệu năng (Performance)                            (Existing — cần bổ sung chỉ số)
    3.4.2 Bảo mật (Security)                                 (Existing — cần bổ sung chỉ số)
    3.4.3 Khả năng mở rộng (Scalability)                     (Existing — cần bổ sung chỉ số)
    3.4.4 Tính sẵn sàng (Availability)                       (Existing — cần bổ sung chỉ số)
    3.4.5 Khả năng sử dụng (Usability)                       (Existing — cần bổ sung chỉ số)
    3.4.6 Khả năng bảo trì (Maintainability)                 (Existing — cần bổ sung chỉ số)

3.5 Phụ lục yêu cầu (Requirement Appendix)
    3.5.1 Quy tắc nghiệp vụ (Business Rules)                 (Existing)


╔══════════════════════════════════════════════════════════════╗
║  IV. MÔ TẢ THIẾT KẾ PHẦN MỀM                              ║
║      (Software Design Description)                          ║
╚══════════════════════════════════════════════════════════════╝

4.1 Thiết kế hệ thống (System Design)
    4.1.1 Kiến trúc hệ thống (Architecture Diagram)           (Existing)
    4.1.2 Kiến trúc triển khai (Deployment Diagram)            (Existing)
    4.1.3 Component / Package Diagram                          (Need to Create)
    4.1.4 Công nghệ sử dụng (Technology Stack)                 (Need to Create)

4.2 Thiết kế cơ sở dữ liệu (Database Design)
    4.2.1 Sơ đồ quan hệ thực thể (ERD)                        (Existing)
    4.2.2 Chi tiết các bảng dữ liệu (Data Dictionary)
          Bảng Roles                                           (Existing)
          Bảng Users                                           (Existing)
          Bảng Series                                          (Existing)
          Bảng Chapters                                        (Existing)
          Bảng Pages                                           (Existing)
          Bảng Tasks                                           (Existing)
          Bảng Submissions                                     (Existing)
          Bảng Reviews                                         (Existing)
          Bảng Series_Rankings                                 (Existing)
          Bảng Notifications                                   (Existing)
    4.2.3 Mô tả mối quan hệ giữa các thực thể                (Existing)

4.3 Thiết kế chi tiết (Detailed Design)
    4.3.1 Thiết kế quy trình nghiệp vụ
          Swimlane — Quy trình sáng tác & xuất bản Manga     (Need to Move — từ 03_2)
          Activity Diagram — Giao và thực hiện Task            (Need to Move — từ 03_2)
          Activity Diagram — Review Chapter                    (Need to Move — từ 03_2)
          Activity Diagram — Xuất bản Manga                    (Need to Move — từ 03_2)

    4.3.2 Thiết kế Sequence Diagram
          Sequence — Đăng nhập hệ thống                       (Existing)
          Sequence — Phân công Task                            (Existing)
          Sequence — Nộp Submission                            (Existing)
          Sequence — Review Chapter                            (Existing)
          Sequence — Xuất bản Manga                            (Existing)

    4.3.3 Thiết kế Class Diagram
          Chi tiết các lớp trong hệ thống
              Lớp Role                                         (Existing)
              Lớp User                                         (Existing)
              Lớp Series                                       (Existing)
              Lớp Chapter                                      (Existing)
              Lớp Page                                         (Existing)
              Lớp Task                                         (Existing)
              Lớp Submission                                   (Existing)
              Lớp Review                                       (Existing)
              Lớp SeriesRanking                                (Existing)
              Lớp Notification                                 (Existing)
          Bổ sung phương thức (Methods)                        (Need to Create)
          Class Diagram tổng thể                               (Existing)
          Mô tả các mối quan hệ                               (Existing)

    4.3.4 Thiết kế giao diện người dùng (UI Design)
          Dashboard                                            (Need to Create)
          Trang đăng nhập                                      (Need to Create)
          Quản lý Series                                       (Need to Create)
          Quản lý Chapter                                      (Need to Create)
          Quản lý Task                                         (Need to Create)
          Nộp Submission                                       (Need to Create)
          Review                                               (Need to Create)
          Thông báo                                            (Need to Create)
          Xếp hạng                                             (Need to Create)


╔══════════════════════════════════════════════════════════════╗
║  V. TÀI LIỆU KIỂM THỬ PHẦN MỀM                           ║
║     (Software Testing Documentation)                        ║
╚══════════════════════════════════════════════════════════════╝

5.1 Phạm vi kiểm thử (Scope of Testing)                       (Need to Create)

5.2 Chiến lược kiểm thử (Test Strategy)                       (Need to Create)

5.3 Kế hoạch kiểm thử (Test Plan)                             (Need to Create)

5.4 Kịch bản kiểm thử (Test Cases)
    TC-01 Đăng nhập — thông tin hợp lệ                        (Existing — cần mở rộng)
    TC-02 Đăng nhập — mật khẩu sai                            (Existing — cần mở rộng)
    TC-03 Đăng nhập — tài khoản bị khóa                       (Need to Create)
    TC-04 Tạo Series mới                                       (Need to Create)
    TC-05 Cập nhật Series                                      (Need to Create)
    TC-06 Tạo Chapter                                          (Need to Create)
    TC-07 Phân công Task cho Assistant                         (Need to Create)
    TC-08 Nộp Submission                                       (Need to Create)
    TC-09 Review Submission — Chấp nhận                        (Need to Create)
    TC-10 Review Submission — Yêu cầu chỉnh sửa               (Need to Create)
    TC-11 Xét duyệt Series mới                                (Need to Create)
    TC-12 Xuất bản Chapter                                     (Need to Create)
    TC-13 Nhập dữ liệu bình chọn                              (Need to Create)
    TC-14 Xem bảng xếp hạng                                   (Need to Create)
    TC-15 Phân quyền — Truy cập trái phép                     (Need to Create)

5.5 Báo cáo kiểm thử (Test Reports)                           (Need to Create)


╔══════════════════════════════════════════════════════════════╗
║  VI. GÓI PHÁT HÀNH & HƯỚNG DẪN SỬ DỤNG                    ║
║      (Release Package & User Guides)                        ║
╚══════════════════════════════════════════════════════════════╝

6.1 Danh sách sản phẩm bàn giao (Deliverable Package)         (Need to Create)

6.2 Hướng dẫn cài đặt (Installation Guides)
    6.2.1 Yêu cầu hệ thống                                    (Need to Create)
    6.2.2 Cài đặt môi trường phát triển                        (Need to Create)
    6.2.3 Cài đặt cơ sở dữ liệu                               (Need to Create)

6.3 Hướng dẫn sử dụng (User Manual)
    6.3.1 Hướng dẫn cho Admin                                  (Need to Create)
    6.3.2 Hướng dẫn cho Mangaka                                (Need to Create)
    6.3.3 Hướng dẫn cho Assistant                              (Need to Create)
    6.3.4 Hướng dẫn cho Tantou Editor                          (Need to Create)
    6.3.5 Hướng dẫn cho Editorial Board                        (Need to Create)


╔══════════════════════════════════════════════════════════════╗
║  PHẦN KẾT                                                   ║
╚══════════════════════════════════════════════════════════════╝

Kết luận và hướng phát triển                                   (Need to Create)
    Tổng kết kết quả đạt được
    Hạn chế của hệ thống
    Hướng phát triển trong tương lai

Tài liệu tham khảo (References)                               (Existing)

Phụ lục
    A. Tài liệu API                                           (Existing — cần mở rộng)
```

---

## BẢNG TỔNG HỢP PHÂN CÔNG

### I. Giới thiệu dự án

| Mục | Existing | Need to Move | Need to Create |
|---|:---:|:---:|:---:|
| 1.1.1 Thông tin dự án | ✅ | | |
| 1.1.2 Nhóm thực hiện | ✅ | | |
| 1.2.1 Thực trạng hiện nay | ✅ | | |
| 1.2.2 Vấn đề cần giải quyết | ✅ | | |
| 1.3.1 Phân tích hệ thống quản lý thủ công | | | ✅ |
| 1.3.2 Phân tích hệ thống quản lý dự án phổ biến | | | ✅ |
| 1.4 Cơ hội phát triển | | | ✅ |
| 1.5.1 Mục tiêu hệ thống | ✅ | | |
| 1.5.2 Giá trị mang lại | ✅ | | |
| 1.6.1 Chức năng chính (5 Actor) | ✅ | | |
| 1.6.2 Giới hạn hệ thống | ✅ | | |
| 1.6.3 Giả định và ràng buộc | ✅ | | |
| **Tổng Chương I** | **9** | **0** | **3** |

---

### II. Kế hoạch quản lý dự án

| Mục | Existing | Need to Move | Need to Create |
|---|:---:|:---:|:---:|
| 2.1.1 Phạm vi và ước lượng | | | ✅ |
| 2.1.2 Mục tiêu dự án | | | ✅ |
| 2.1.3 Rủi ro dự án | | | ✅ |
| 2.2.1 Quy trình phát triển | | | ✅ |
| 2.2.2 Quản lý chất lượng | | | ✅ |
| 2.3 Sản phẩm bàn giao | | | ✅ |
| 2.4 Phân công trách nhiệm | | | ✅ |
| 2.5 Giao tiếp dự án | | | ✅ |
| 2.6.1 Quản lý tài liệu | | | ✅ |
| 2.6.2 Quản lý mã nguồn | | | ✅ |
| 2.6.3 Công cụ và hạ tầng | | | ✅ |
| **Tổng Chương II** | **0** | **0** | **11** |

---

### III. Đặc tả yêu cầu phần mềm (SRS)

| Mục | Existing | Need to Move | Need to Create |
|---|:---:|:---:|:---:|
| 3.1.1 Mô tả hệ thống | ✅ | | |
| 3.1.2 Context Diagram | | | ✅ |
| 3.1.3 Quy trình nghiệp vụ tổng quát | ✅ | | |
| 3.2.1 Danh sách Actor | | ✅ | |
| 3.2.2 Use Case Diagram (7 diagram) | | ✅ | |
| 3.2.3 Bảng tóm tắt Use Case | | | ✅ |
| 3.2.4 Yêu cầu từng nhóm người dùng (5 actor) | ✅ | | |
| 3.3.1 System Functional Overview (4 mục) | | | ✅ |
| 3.3.2 UC-01, UC-02 (Authentication) | | | ✅ |
| 3.3.3 UC-03→UC-06 (User Management) | | | ✅ |
| 3.3.4 UC-07→UC-10 (Series Management) | | | ✅ |
| 3.3.5 UC-11→UC-13 (Chapter Management) | | | ✅ |
| 3.3.6 UC-14→UC-15 (Page Management) | | | ✅ |
| 3.3.7 UC-16→UC-19 (Task Management) | | | ✅ |
| 3.3.8 UC-20→UC-22 (Submission Management) | | | ✅ |
| 3.3.9 UC-23→UC-25 (Review Management) | | | ✅ |
| 3.3.10 UC-26→UC-28 (Approval & Publishing) | | | ✅ |
| 3.3.11 UC-29→UC-31 (Ranking Management) | | | ✅ |
| 3.3.12 UC-32→UC-33 (Notification Management) | | | ✅ |
| 3.4.1 Hiệu năng | ✅ *(cần bổ sung chỉ số)* | | |
| 3.4.2 Bảo mật | ✅ *(cần bổ sung chỉ số)* | | |
| 3.4.3 Khả năng mở rộng | ✅ *(cần bổ sung chỉ số)* | | |
| 3.4.4 Tính sẵn sàng | ✅ *(cần bổ sung chỉ số)* | | |
| 3.4.5 Khả năng sử dụng | ✅ *(cần bổ sung chỉ số)* | | |
| 3.4.6 Khả năng bảo trì | ✅ *(cần bổ sung chỉ số)* | | |
| 3.5.1 Quy tắc nghiệp vụ | ✅ | | |
| **Tổng Chương III** | **10** | **2** | **14** |

---

### IV. Mô tả thiết kế phần mềm (SDD)

| Mục | Existing | Need to Move | Need to Create |
|---|:---:|:---:|:---:|
| 4.1.1 Kiến trúc hệ thống | ✅ | | |
| 4.1.2 Kiến trúc triển khai | ✅ | | |
| 4.1.3 Component / Package Diagram | | | ✅ |
| 4.1.4 Công nghệ sử dụng | | | ✅ |
| 4.2.1 ERD | ✅ | | |
| 4.2.2 Data Dictionary (10 bảng) | ✅ | | |
| 4.2.3 Mô tả mối quan hệ | ✅ | | |
| 4.3.1 Swimlane + 3 Activity Diagram | | ✅ | |
| 4.3.2 Sequence Diagram (5 diagram) | ✅ | | |
| 4.3.3 Class Diagram + 10 lớp + quan hệ | ✅ | | |
| 4.3.3 Bổ sung Methods cho các lớp | | | ✅ |
| 4.3.4 UI Design (9 màn hình) | | | ✅ |
| **Tổng Chương IV** | **7** | **1** | **4** |

---

### V. Tài liệu kiểm thử

| Mục | Existing | Need to Move | Need to Create |
|---|:---:|:---:|:---:|
| 5.1 Phạm vi kiểm thử | | | ✅ |
| 5.2 Chiến lược kiểm thử | | | ✅ |
| 5.3 Kế hoạch kiểm thử | | | ✅ |
| 5.4 TC-01, TC-02 | ✅ *(cần mở rộng)* | | |
| 5.4 TC-03→TC-15 | | | ✅ |
| 5.5 Báo cáo kiểm thử | | | ✅ |
| **Tổng Chương V** | **1** | **0** | **5** |

---

### VI. Gói phát hành & Hướng dẫn sử dụng

| Mục | Existing | Need to Move | Need to Create |
|---|:---:|:---:|:---:|
| 6.1 Deliverable Package | | | ✅ |
| 6.2.1 Yêu cầu hệ thống | | | ✅ |
| 6.2.2 Cài đặt môi trường | | | ✅ |
| 6.2.3 Cài đặt CSDL | | | ✅ |
| 6.3.1–6.3.5 User Manual (5 Actor) | | | ✅ |
| **Tổng Chương VI** | **0** | **0** | **5** |

---

### Phần kết + Phụ lục

| Mục | Existing | Need to Move | Need to Create |
|---|:---:|:---:|:---:|
| Kết luận & hướng phát triển | | | ✅ |
| Tài liệu tham khảo | ✅ | | |
| Phụ lục A — API | ✅ *(cần mở rộng)* | | |
| **Tổng** | **2** | **0** | **1** |

---

## TỔNG KẾT

| | Existing | Need to Move | Need to Create | Tổng |
|---|:---:|:---:|:---:|:---:|
| **Chương I** | 9 | 0 | 3 | 12 |
| **Chương II** | 0 | 0 | 11 | 11 |
| **Chương III** | 10 | 2 | 14 | 26 |
| **Chương IV** | 7 | 1 | 4 | 12 |
| **Chương V** | 1 | 0 | 5 | 6 |
| **Chương VI** | 0 | 0 | 5 | 5 |
| **Kết + Phụ lục** | 2 | 0 | 1 | 3 |
| **TỔNG** | **29** | **3** | **43** | **75** |

> [!WARNING]
> **Lưu ý quan trọng trước khi bắt đầu:**
> - **3 mục Need to Move** — Use Case Diagram, Actor List (từ Chương III cũ → III SRS mới), Activity/Swimlane (từ Chương III cũ → IV SDD mới)
> - **43 mục Need to Create** — phần lớn là UC Specification (33 UC) và Testing (15 TC)
> - **File `03_3_uml_thiet_ke.tex` có nội dung trùng lặp** (Sequence section bị copy-paste 2 lần) — cần xóa bản trùng trước khi di chuyển
>
> **Câu hỏi cần quyết định:**
> 1. **Chương II (SPMP)** — Giữ hay bỏ?
> 2. **UC Specification** — Viết chi tiết cả 33 UC hay chỉ 7–10 UC chính (phần còn lại viết dạng bảng tóm tắt)?
> 3. **UI Design** — Dùng screenshot thực tế hay vẽ wireframe?
