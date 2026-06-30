# PROJECT DOCUMENT CHECKLIST

## Manga Creation Workflow and Publishing Management System

---

# 📍 Giai đoạn 1: Khảo sát đề tài và thu thập yêu cầu

### ✅ 1. Tổng quan đề tài
* [x] Xác định tên đề tài
* [x] Viết mô tả dự án
* [x] Xác định mục tiêu hệ thống
* [x] Xác định phạm vi hệ thống
* [x] Xác định giá trị thực tiễn của đề tài

---

### ✅ 2. Nhóm thực hiện
* [x] Liệt kê thành viên nhóm
* [x] Phân chia vai trò
* [x] Phân chia công việc
* [x] Kiểm tra thông tin liên hệ

---

### ✅ 3. Bối cảnh đề tài
* [x] Phân tích thực trạng hiện nay
* [x] Xác định các vấn đề tồn tại
* [x] Phân tích nhu cầu quản lý
* [x] Xác định bài toán thực tế

---

### ✅ 4. Tầm nhìn hệ thống
* [x] Xác định mục tiêu hệ thống
* [x] Xác định định hướng phát triển
* [x] Xác định giá trị hệ thống mang lại
* [x] Xác định lợi ích cho người dùng

---

### ✅ 5. Đối tượng sử dụng
* [x] Xác định Actor của hệ thống
* [x] Mô tả vai trò Admin
* [x] Mô tả vai trò Mangaka
* [x] Mô tả vai trò Assistant
* [x] Mô tả vai trò Tantou Editor
* [x] Mô tả vai trò Editorial Board

---

### ✅ 6. Phạm vi và giới hạn hệ thống
* [x] Xác định phạm vi dự án
* [x] Liệt kê chức năng chính
* [x] Xác định giới hạn hệ thống
* [x] Xác định giả định hệ thống
* [x] Xác định ràng buộc hệ thống

---

# 🎯 Kết quả đầu ra Giai đoạn 1
* [x] Hoàn thiện Chương I
* [x] Hoàn thiện mô tả bài toán
* [x] Xác định rõ phạm vi hệ thống
* [x] Xác định đầy đủ Actor và nghiệp vụ

---

# 📍 Giai đoạn 2: Phân tích chi tiết yêu cầu hệ thống

## ✅ 1. Tổng quan hệ thống
* [x] Viết mô tả hệ thống
* [x] Xác định các bên liên quan
* [x] Mô tả quy trình nghiệp vụ tổng quát

---

## ✅ 2. Yêu cầu người dùng

### Admin
* [x] Phân tích yêu cầu Admin

### Mangaka
* [x] Phân tích yêu cầu Mangaka

### Assistant
* [x] Phân tích yêu cầu Assistant

### Tantou Editor
* [x] Phân tích yêu cầu Tantou Editor

### Editorial Board
* [x] Phân tích yêu cầu Editorial Board

---

## ✅ 3. Yêu cầu chức năng
* [x] Quản lý người dùng và phân quyền
* [x] Quản lý Series
* [x] Quản lý Chapter
* [x] Quản lý Page
* [x] Quản lý Task
* [x] Quản lý Submission
* [x] Quản lý Review
* [x] Quản lý phát hành
* [x] Quản lý Ranking
* [x] Quản lý Notification

---

## ✅ 4. Yêu cầu phi chức năng
* [x] Hiệu năng
* [x] Bảo mật
* [x] Khả năng mở rộng
* [x] Tính sẵn sàng
* [x] Khả năng sử dụng
* [x] Khả năng bảo trì

---

## ✅ 5. Quy tắc nghiệp vụ
* [x] Quy tắc quản lý Series
* [x] Quy tắc quản lý Chapter
* [x] Quy tắc quản lý Task
* [x] Quy tắc quản lý Submission
* [x] Quy tắc quản lý Review
* [x] Quy tắc xuất bản
* [x] Quy tắc xếp hạng
* [x] Quy tắc phân quyền

---

# 🎯 Kết quả đầu ra Giai đoạn 2
* [x] Hoàn thiện Chương II
* [x] Hoàn thiện yêu cầu chức năng
* [x] Hoàn thiện yêu cầu phi chức năng
* [x] Hoàn thiện Business Rules
* [x] Kiểm tra consistency giữa yêu cầu và nghiệp vụ

---

# 📍 Giai đoạn 3: Thiết kế sơ đồ UML & Quy trình nghiệp vụ

## ✅ 1. Thiết kế kiến trúc hệ thống
* [x] Thiết kế Three-Tier Architecture
* [x] Thiết kế Client-Server Architecture
* [x] Thiết kế mô hình triển khai hệ thống
* [x] Kiểm tra tính mở rộng kiến trúc

---

## ✅ 2. Thiết kế Use Case Diagram

### Tổng thể
* [x] Danh sách Actor
* [x] Use Case Diagram tổng thể

### Chi tiết
* [x] Use Case Admin
* [x] Use Case Mangaka
* [x] Use Case Assistant
* [x] Use Case Tantou Editor
* [x] Use Case Editorial Board

---

## ✅ 3. Thiết kế quy trình nghiệp vụ

### Swimlane Diagram
* [x] Swimlane tổng quát

### Activity Diagram
* [x] Quy trình giao Task
* [x] Quy trình thực hiện Task
* [x] Quy trình Review Chapter
* [x] Quy trình xuất bản Manga

---

## ✅ 4. Thiết kế Sequence Diagram
* [x] Sequence Login
* [x] Sequence Assign Task
* [x] Sequence Submit Submission
* [x] Sequence Review Chapter
* [x] Sequence Publish Manga

---

# 🎯 Kết quả đầu ra Giai đoạn 3
* [x] Hoàn thiện toàn bộ UML nghiệp vụ
* [x] Hoàn thiện Use Case Diagram
* [x] Hoàn thiện Activity Diagram
* [x] Hoàn thiện Sequence Diagram
* [x] Kiểm tra consistency giữa UML và yêu cầu hệ thống

---

# 📍 Giai đoạn 4: Thiết kế Class Diagram & Cơ sở dữ liệu

## ✅ 1. Thiết kế Class Diagram
* [x] Mô tả lớp Ranking
* [x] Mô tả lớp Notification

---

## ✅ 2. Thiết kế cơ sở dữ liệu
* [x] Thiết kế ERD
* [x] Xác định Primary Key
* [x] Xác định Foreign Key
* [x] Chuẩn hóa dữ liệu
* [x] Kiểm tra ràng buộc dữ liệu

---

## ✅ 3. Mô tả quan hệ dữ liệu
* [x] Quan hệ Role - User
* [x] Quan hệ User - Series
* [x] Quan hệ Series - Chapter
* [x] Quan hệ Chapter - Page
* [x] Quan hệ Page - Task
* [x] Quan hệ Task - Submission
* [x] Quan hệ Submission - Review
* [x] Quan hệ Series - Ranking
* [x] Quan hệ User - Notification

---

# 🎯 Kết quả đầu ra Giai đoạn 4
* [x] Hoàn thiện Class Diagram
* [x] Hoàn thiện ERD
* [x] Hoàn thiện Database Design
* [x] Kiểm tra consistency giữa Database và UML

---

# 📍 Giai đoạn 5: Tổng hợp, biên soạn và chuẩn hóa tài liệu

## ✅ 1. Tổng hợp tài liệu
* [ ] Tổng hợp Chương I
* [ ] Tổng hợp Chương II
* [ ] Tổng hợp Chương III
* [ ] Đồng bộ nội dung giữa các chương

---

## ✅ 2. Chuẩn hóa LaTeX
* [ ] Kiểm tra format tiêu đề
* [ ] Kiểm tra numbering
* [ ] Kiểm tra mục lục
* [ ] Kiểm tra danh sách hình
* [ ] Kiểm tra danh sách bảng
* [ ] Kiểm tra font chữ
* [ ] Kiểm tra căn lề
* [ ] Kiểm tra spacing

---

## ✅ 3. Kiểm tra Diagram
* [ ] Kiểm tra chất lượng hình ảnh
* [ ] Kiểm tra tên hình
* [ ] Kiểm tra mô tả hình
* [ ] Kiểm tra numbering Diagram
* [ ] Kiểm tra UML consistency

---

# 🎯 Kết quả đầu ra Giai đoạn 5
* [ ] Hoàn thiện tài liệu LaTeX
* [ ] Build PDF thành công
* [ ] Không lỗi format
* [ ] Không lỗi numbering

---

# 📍 Giai đoạn 6: Kiểm tra, tối ưu hóa và hoàn thiện cuối cùng

## ✅ 1. Review nội dung
* [ ] Kiểm tra lỗi chính tả
* [ ] Kiểm tra thuật ngữ
* [ ] Kiểm tra consistency nội dung
* [ ] Kiểm tra logic nghiệp vụ

---

## ✅ 2. Review kỹ thuật
* [ ] Kiểm tra UML consistency
* [ ] Kiểm tra Database consistency
* [ ] Kiểm tra Use Case consistency
* [ ] Kiểm tra Business Rule consistency

---

## ✅ 3. Chuẩn bị bảo vệ
* [ ] Chuẩn bị Slide
* [ ] Chuẩn bị Script thuyết trình
* [ ] Chuẩn bị Demo
* [ ] Chuẩn bị Q&A

---

## ✅ 4. Final Submission
* [ ] Kiểm tra file PDF cuối cùng
* [ ] Kiểm tra source LaTeX
* [ ] Backup GitHub
* [ ] Kiểm tra thư mục nộp bài
* [ ] Nộp tài liệu chính thức

---

# 🎯 Kết quả đầu ra Giai đoạn 6
* [ ] Hoàn thiện tài liệu cuối cùng
* [ ] Hoàn thiện slide bảo vệ
* [ ] Sẵn sàng demo hệ thống
* [ ] Sẵn sàng bảo vệ đồ án
