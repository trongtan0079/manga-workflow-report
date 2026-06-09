# PROJECT DOCUMENT CHECKLIST

## Manga Creation Workflow and Publishing Management System

---

# 📍 Giai đoạn 1: Khảo sát đề tài và thu thập yêu cầu

### ✅ 1. Tổng quan đề tài
* [ ] Xác định tên đề tài
* [ ] Viết mô tả dự án
* [ ] Xác định mục tiêu hệ thống
* [ ] Xác định phạm vi hệ thống
* [ ] Xác định giá trị thực tiễn của đề tài

---

### ✅ 2. Nhóm thực hiện
* [ ] Liệt kê thành viên nhóm
* [ ] Phân chia vai trò
* [ ] Phân chia công việc
* [ ] Kiểm tra thông tin liên hệ

---

### ✅ 3. Bối cảnh đề tài
* [ ] Phân tích thực trạng hiện nay
* [ ] Xác định các vấn đề tồn tại
* [ ] Phân tích nhu cầu quản lý
* [ ] Xác định bài toán thực tế

---

### ✅ 4. Tầm nhìn hệ thống
* [ ] Xác định mục tiêu hệ thống
* [ ] Xác định định hướng phát triển
* [ ] Xác định giá trị hệ thống mang lại
* [ ] Xác định lợi ích cho người dùng

---

### ✅ 5. Đối tượng sử dụng
* [ ] Xác định Actor của hệ thống
* [ ] Mô tả vai trò Admin
* [ ] Mô tả vai trò Mangaka
* [ ] Mô tả vai trò Assistant
* [ ] Mô tả vai trò Tantou Editor
* [ ] Mô tả vai trò Editorial Board

---

### ✅ 6. Phạm vi và giới hạn hệ thống
* [ ] Xác định phạm vi dự án
* [ ] Liệt kê chức năng chính
* [ ] Xác định giới hạn hệ thống
* [ ] Xác định giả định hệ thống
* [ ] Xác định ràng buộc hệ thống

---

# 🎯 Kết quả đầu ra Giai đoạn 1
* [ ] Hoàn thiện Chương I
* [ ] Hoàn thiện mô tả bài toán
* [ ] Xác định rõ phạm vi hệ thống
* [ ] Xác định đầy đủ Actor và nghiệp vụ

---

# 📍 Giai đoạn 2: Phân tích chi tiết yêu cầu hệ thống

## ✅ 1. Tổng quan hệ thống
* [ ] Viết mô tả hệ thống
* [ ] Xác định các bên liên quan
* [ ] Mô tả quy trình nghiệp vụ tổng quát

---

## ✅ 2. Yêu cầu người dùng

### Admin
* [ ] Phân tích yêu cầu Admin

### Mangaka
* [ ] Phân tích yêu cầu Mangaka

### Assistant
* [ ] Phân tích yêu cầu Assistant

### Tantou Editor
* [ ] Phân tích yêu cầu Tantou Editor

### Editorial Board
* [ ] Phân tích yêu cầu Editorial Board

---

## ✅ 3. Yêu cầu chức năng
* [ ] Quản lý người dùng và phân quyền
* [ ] Quản lý Series
* [ ] Quản lý Chapter
* [ ] Quản lý Page
* [ ] Quản lý Task
* [ ] Quản lý Submission
* [ ] Quản lý Review
* [ ] Quản lý phát hành
* [ ] Quản lý Ranking
* [ ] Quản lý Notification

---

## ✅ 4. Yêu cầu phi chức năng
* [ ] Hiệu năng
* [ ] Bảo mật
* [ ] Khả năng mở rộng
* [ ] Tính sẵn sàng
* [ ] Khả năng sử dụng
* [ ] Khả năng bảo trì

---

## ✅ 5. Quy tắc nghiệp vụ
* [ ] Quy tắc quản lý Series
* [ ] Quy tắc quản lý Chapter
* [ ] Quy tắc quản lý Task
* [ ] Quy tắc quản lý Submission
* [ ] Quy tắc quản lý Review
* [ ] Quy tắc xuất bản
* [ ] Quy tắc xếp hạng
* [ ] Quy tắc phân quyền

---

# 🎯 Kết quả đầu ra Giai đoạn 2
* [ ] Hoàn thiện Chương II
* [ ] Hoàn thiện yêu cầu chức năng
* [ ] Hoàn thiện yêu cầu phi chức năng
* [ ] Hoàn thiện Business Rules
* [ ] Kiểm tra consistency giữa yêu cầu và nghiệp vụ

---

# 📍 Giai đoạn 3: Thiết kế sơ đồ UML & Quy trình nghiệp vụ

## ✅ 1. Thiết kế kiến trúc hệ thống
* [ ] Thiết kế Three-Tier Architecture
* [ ] Thiết kế Client-Server Architecture
* [ ] Thiết kế mô hình triển khai hệ thống
* [ ] Kiểm tra tính mở rộng kiến trúc

---

## ✅ 2. Thiết kế Use Case Diagram

### Tổng thể
* [ ] Danh sách Actor
* [ ] Use Case Diagram tổng thể

### Chi tiết
* [ ] Use Case Admin
* [ ] Use Case Mangaka
* [ ] Use Case Assistant
* [ ] Use Case Tantou Editor
* [ ] Use Case Editorial Board

---

## ✅ 3. Thiết kế quy trình nghiệp vụ

### Swimlane Diagram
* [ ] Swimlane tổng quát

### Activity Diagram
* [ ] Quy trình giao Task
* [ ] Quy trình thực hiện Task
* [ ] Quy trình Review Chapter
* [ ] Quy trình xuất bản Manga

---

## ✅ 4. Thiết kế Sequence Diagram
* [ ] Sequence Login
* [ ] Sequence Assign Task
* [ ] Sequence Submit Submission
* [ ] Sequence Review Chapter
* [ ] Sequence Publish Manga

---

# 🎯 Kết quả đầu ra Giai đoạn 3
* [ ] Hoàn thiện toàn bộ UML nghiệp vụ
* [ ] Hoàn thiện Use Case Diagram
* [ ] Hoàn thiện Activity Diagram
* [ ] Hoàn thiện Sequence Diagram
* [ ] Kiểm tra consistency giữa UML và yêu cầu hệ thống

---

# 📍 Giai đoạn 4: Thiết kế Class Diagram & Cơ sở dữ liệu

## ✅ 1. Thiết kế Class Diagram
* [ ] Class Diagram tổng thể
* [ ] Mô tả lớp User
* [ ] Mô tả lớp Role
* [ ] Mô tả lớp Series
* [ ] Mô tả lớp Chapter
* [ ] Mô tả lớp Page
* [ ] Mô tả lớp Task
* [ ] Mô tả lớp Submission
* [ ] Mô tả lớp Review
* [ ] Mô tả lớp Ranking
* [ ] Mô tả lớp Notification

---

## ✅ 2. Thiết kế cơ sở dữ liệu
* [ ] Thiết kế ERD
* [ ] Xác định Primary Key
* [ ] Xác định Foreign Key
* [ ] Chuẩn hóa dữ liệu
* [ ] Kiểm tra ràng buộc dữ liệu

---

## ✅ 3. Mô tả quan hệ dữ liệu
* [ ] Quan hệ Role - User
* [ ] Quan hệ User - Series
* [ ] Quan hệ Series - Chapter
* [ ] Quan hệ Chapter - Page
* [ ] Quan hệ Page - Task
* [ ] Quan hệ Task - Submission
* [ ] Quan hệ Submission - Review
* [ ] Quan hệ Series - Ranking
* [ ] Quan hệ User - Notification

---

# 🎯 Kết quả đầu ra Giai đoạn 4
* [ ] Hoàn thiện Class Diagram
* [ ] Hoàn thiện ERD
* [ ] Hoàn thiện Database Design
* [ ] Kiểm tra consistency giữa Database và UML

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
