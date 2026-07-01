# coding=utf-8
import os

TEMPLATE = r"""\begin{table}[H]
\centering
\renewcommand{\arraystretch}{1.3}
\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}p{4.5cm}|>{\raggedright\arraybackslash}X|}
\hline
\rowcolor{tableheader}
\multicolumn{2}{|c|}{\textbf{Đặc tả Use Case: [[name]]}} \\ \hline
\textbf{Mã Use Case} & [[id]] \\ \hline
\textbf{Tên Use Case} & [[name]] \\ \hline
\textbf{Actor chính} & [[actor]] \\ \hline
\textbf{Mô tả} & [[desc]] \\ \hline
\textbf{Tiền điều kiện (Pre-conditions)} & [[pre]] \\ \hline
\textbf{Luồng sự kiện chính (Basic Flow)} & 
\begin{minipage}[t]{\linewidth}
    \begin{enumerate}[leftmargin=*]
[[basic]]
    \end{enumerate}
\end{minipage} \\ \hline
\textbf{Luồng rẽ nhánh/Ngoại lệ (Alternate/Exception)} & 
\begin{minipage}[t]{\linewidth}
    \begin{itemize}[leftmargin=*]
[[alt]]
    \end{itemize}
\end{minipage} \\ \hline
\textbf{Hậu điều kiện (Post-conditions)} & [[post]] \\ \hline
\end{tabularx}
\caption{Đặc tả [[id]]: [[name]]}
\label{tab:[[label]]}
\end{table}
"""

ucs = [
    {
        "sec": r"\subsection{Quản lý Chapter (Chapter Management)}\label{subsec:srs_chapter_mgmt}",
        "sub": r"\subsubsection{UC-11: Tạo Chapter mới}\label{subsubsec:uc11_create_chapter}",
        "id": "UC-11", "name": "Tạo Chapter mới", "actor": "Mangaka", "label": "uc11",
        "desc": "Cho phép Mangaka tạo một Chapter mới thuộc về một Series cụ thể.",
        "pre": "Tài khoản Mangaka ở trạng thái Active và đã được cấp quyền quản lý nội dung của Series tương ứng.",
        "basic": r"        \item Mangaka chọn Series cần thêm Chapter." + "\n" + r"        \item Mangaka chọn chức năng 'Thêm Chapter mới'." + "\n" + r"        \item Hệ thống hiển thị form nhập liệu." + "\n" + r"        \item Mangaka nhập thông tin (Số thứ tự lớn hơn 0, Tiêu đề tối đa 100 ký tự, Số trang dự kiến)." + "\n" + r"        \item Mangaka nhấn 'Lưu'." + "\n" + r"        \item Hệ thống xác thực dữ liệu, lưu thông tin và hiển thị thông báo thành công.",
        "alt": r"        \item \textbf{A1}: Thông tin không hợp lệ (trùng số thứ tự). Hệ thống báo lỗi chữ đỏ và tự động gợi ý số thứ tự Chapter hợp lệ kế tiếp.",
        "post": "Một Chapter mới được tạo trong hệ thống với trạng thái 'Bản nháp' (Draft)."
    },
    {
        "sub": r"\subsubsection{UC-12: Cập nhật thông tin Chapter}\label{subsubsec:uc12_update_chapter}",
        "id": "UC-12", "name": "Cập nhật thông tin Chapter", "actor": "Mangaka", "label": "uc12",
        "desc": "Cho phép Mangaka chỉnh sửa thông tin của Chapter đã tạo (tiêu đề, số trang dự kiến).",
        "pre": "Mangaka có quyền quản lý Series và Chapter phải đang ở trạng thái cho phép chỉnh sửa (chưa xuất bản).",
        "basic": r"        \item Mangaka chọn Chapter cần chỉnh sửa." + "\n" + r"        \item Hệ thống hiển thị thông tin hiện tại của Chapter." + "\n" + r"        \item Mangaka thay đổi thông tin." + "\n" + r"        \item Mangaka nhấn 'Cập nhật'." + "\n" + r"        \item Hệ thống kiểm tra tính hợp lệ, lưu thay đổi và hiển thị thông báo thành công.",
        "alt": r"        \item \textbf{A1}: Chapter đã xuất bản. Hệ thống khóa (disable) các trường quan trọng (số thứ tự) và hiển thị thông báo 'Chỉ được sửa tiêu đề phụ'.",
        "post": "Thông tin Chapter được cập nhật đồng bộ trong cơ sở dữ liệu."
    },
    {
        "sub": r"\subsubsection{UC-13: Theo dõi tiến độ Chapter}\label{subsubsec:uc13_track_chapter}",
        "id": "UC-13", "name": "Theo dõi tiến độ Chapter", "actor": "Mangaka, Tantou Editor", "label": "uc13",
        "desc": "Xem tổng quan tiến độ hoàn thành các trang và công việc (Task) trong Chapter.",
        "pre": "Tài khoản ở trạng thái Active và có quyền xem báo cáo của Series tương ứng.",
        "basic": r"        \item Người dùng chọn Chapter cần theo dõi." + "\n" + r"        \item Người dùng chọn 'Tiến độ'." + "\n" + r"        \item Hệ thống tính toán và hiển thị % hoàn thành dựa trên số Task/Page đã chuyển sang trạng thái 'Completed'." + "\n" + r"        \item Hiển thị danh sách các trang đang thực hiện, đang chờ duyệt bằng biểu đồ trực quan.",
        "alt": r"        \item \textbf{A1}: Chapter chưa có Page hay Task nào. Hệ thống hiển thị 0\% và gợi ý nút 'Tạo Task ngay' hoặc 'Tạo Page mới'.",
        "post": "Người dùng nắm được tình trạng hiện tại của Chapter theo thời gian thực."
    },
    {
        "sec": r"\subsection{Quản lý Page (Page Management)}\label{subsec:srs_page_mgmt}",
        "sub": r"\subsubsection{UC-14: Tạo Page}\label{subsubsec:uc14_create_page}",
        "id": "UC-14", "name": "Tạo Page", "actor": "Mangaka", "label": "uc14",
        "desc": "Cho phép Mangaka tạo các trang trống (Page) trong Chapter để chuẩn bị phân công công việc cho Assistant.",
        "pre": "Mangaka đăng nhập sở hữu bộ truyện chứa Chapter tương ứng.",
        "basic": r"        \item Mangaka vào giao diện chi tiết Chapter." + "\n" + r"        \item Mangaka chọn 'Thêm Page'." + "\n" + r"        \item Hệ thống tự động sinh số thứ tự trang tiếp theo hoặc cho phép nhập số trang hàng loạt (Batch create)." + "\n" + r"        \item Mangaka nhấn 'Lưu'." + "\n" + r"        \item Hệ thống tạo các bản ghi Page tương ứng trong cơ sở dữ liệu.",
        "alt": r"        \item \textbf{A1}: Số lượng Page tạo ra vượt mức 100 trang/chapter. Hệ thống cảnh báo quá tải và yêu cầu xác nhận thêm.",
        "post": "Các trang mới được tạo với trạng thái 'Trống' (Blank), sẵn sàng cho phân công."
    },
    {
        "sub": r"\subsubsection{UC-15: Cập nhật trạng thái Page}\label{subsubsec:uc15_update_page}",
        "id": "UC-15", "name": "Cập nhật trạng thái Page", "actor": "Mangaka, Assistant", "label": "uc15",
        "desc": "Cập nhật trạng thái của trang trong quy trình vẽ (Draft, Inked, Toned, Completed).",
        "pre": "Page đã tồn tại và người dùng có quyền chỉnh sửa Page này (được phân công hoặc là Mangaka).",
        "basic": r"        \item Người dùng chọn Page cụ thể." + "\n" + r"        \item Chọn thay đổi trạng thái từ menu thả xuống (Dropdown)." + "\n" + r"        \item Hệ thống cập nhật trạng thái mới của Page." + "\n" + r"        \item Hệ thống tự động tính toán lại tiến độ tổng của Chapter và lưu lại lịch sử thay đổi.",
        "alt": r"        \item \textbf{A1}: Người dùng không có quyền (không được phân công). Hệ thống chặn thao tác và hiển thị 'Bạn không có quyền chuyển trạng thái trang này'.",
        "post": "Trạng thái Page được lưu vết (Audit log) và tiến độ Chapter thay đổi tương ứng."
    },
    {
        "sec": r"\subsection{Quản lý Task (Task Assignment \& Tracking)}\label{subsec:srs_task_mgmt}",
        "sub": r"\subsubsection{UC-16: Tạo và phân công Task}\label{subsubsec:uc16_create_task}",
        "id": "UC-16", "name": "Tạo và phân công Task", "actor": "Mangaka", "label": "uc16",
        "desc": "Tạo công việc cụ thể (vẽ background, đổ bóng, tone...) và giao cho Assistant.",
        "pre": "Mangaka là người quản lý dự án, danh sách Assistant đã được thêm vào nhóm làm việc.",
        "basic": r"        \item Mangaka chọn Page hoặc Chapter." + "\n" + r"        \item Chọn 'Tạo Task mới'." + "\n" + r"        \item Nhập mô tả công việc (giới hạn 500 ký tự), chọn loại công việc, và ấn định hạn chót (Deadline)." + "\n" + r"        \item Chọn Assistant từ danh sách thành viên nhóm." + "\n" + r"        \item Nhấn 'Phân công'." + "\n" + r"        \item Hệ thống lưu Task, kích hoạt gửi Email/Push Notification cho Assistant.",
        "alt": r"        \item \textbf{A1}: Assistant đang tồn đọng quá 5 Task chưa hoàn thành. Hệ thống hiện cảnh báo 'Assistant đang quá tải' nhưng vẫn cho phép phân công nếu Mangaka xác nhận.",
        "post": "Task chuyển sang trạng thái 'Assigned', Assistant nhận được thông báo ngay lập tức."
    },
    {
        "sub": r"\subsubsection{UC-17: Cập nhật trạng thái Task}\label{subsubsec:uc17_update_task}",
        "id": "UC-17", "name": "Cập nhật trạng thái Task", "actor": "Assistant", "label": "uc17",
        "desc": "Assistant cập nhật tình trạng công việc mình đang làm trên hệ thống Kanban.",
        "pre": "Assistant đã đăng nhập và là người được chỉ định thực hiện Task đó.",
        "basic": r"        \item Assistant vào danh sách 'Task của tôi'." + "\n" + r"        \item Kéo thả Task (hoặc bấm chọn) để thay đổi trạng thái sang 'In Progress', 'Ready for Review' hoặc 'Completed'." + "\n" + r"        \item Hệ thống ghi nhận trạng thái, thời gian cập nhật." + "\n" + r"        \item Thông báo tự động gửi đến Mangaka nếu trạng thái là 'Ready for Review'.",
        "alt": r"        \item \textbf{A1}: Task thuộc về một Series đang bị tạm ngưng (Hiatus). Hệ thống khóa Task và thông báo 'Dự án đang đóng băng, không thể cập nhật'.",
        "post": "Trạng thái Task được thay đổi và lịch sử thao tác được lưu trữ."
    },
    {
        "sub": r"\subsubsection{UC-18: Theo dõi tiến độ Task}\label{subsubsec:uc18_track_task}",
        "id": "UC-18", "name": "Theo dõi tiến độ Task", "actor": "Mangaka", "label": "uc18",
        "desc": "Mangaka xem danh sách toàn bộ Task để đánh giá hiệu suất của nhóm.",
        "pre": "Mangaka có quyền quản lý nhóm làm việc (Team management).",
        "basic": r"        \item Mangaka mở Dashboard của Series." + "\n" + r"        \item Xem danh sách Task dưới dạng Kanban Board (To Do, In Progress, Review, Done)." + "\n" + r"        \item Sử dụng bộ lọc (Filter) theo Assistant, loại công việc, hoặc theo Deadline gần nhất." + "\n" + r"        \item Hệ thống truy vấn và hiển thị các Task đáp ứng tiêu chí lọc ngay lập tức.",
        "alt": r"        \item \textbf{A1}: Chưa có Task nào được tạo. Hệ thống hiện màn hình trống kèm giao diện hướng dẫn (Onboarding) và nút 'Tạo Task đầu tiên'.",
        "post": "Mangaka nắm bắt được nút thắt cổ chai (bottleneck) của nhóm."
    },
    {
        "sub": r"\subsubsection{UC-19: Hủy Task}\label{subsubsec:uc19_cancel_task}",
        "id": "UC-19", "name": "Hủy Task", "actor": "Mangaka", "label": "uc19",
        "desc": "Hủy bỏ một công việc đã phân công do thay đổi kế hoạch kịch bản.",
        "pre": "Task chưa chuyển sang trạng thái 'Completed' hoặc 'Reviewed'.",
        "basic": r"        \item Mangaka chọn Task cần hủy." + "\n" + r"        \item Chọn 'Hủy Task', hệ thống yêu cầu nhập lý do bắt buộc." + "\n" + r"        \item Mangaka nhập lý do và xác nhận." + "\n" + r"        \item Hệ thống đánh dấu Task là 'Cancelled' và gửi thông báo cho Assistant.",
        "alt": r"        \item \textbf{A1}: Task đã ở trạng thái Completed. Nút Hủy bị mờ (disabled), hệ thống gợi ý 'Tạo Task mới để sửa đổi thay vì hủy'.",
        "post": "Task bị vô hiệu hóa, giảm khối lượng công việc hiện tại của Assistant."
    },
    {
        "sec": r"\subsection{Quản lý Submission (Submission Management)}\label{subsec:srs_submission_mgmt}",
        "sub": r"\subsubsection{UC-20: Nộp Submission}\label{subsubsec:uc20_submit}",
        "id": "UC-20", "name": "Nộp Submission", "actor": "Assistant", "label": "uc20",
        "desc": "Nộp kết quả công việc (file ảnh/tài liệu) lên Cloud để Mangaka đánh giá.",
        "pre": "Task đang ở trạng thái 'In Progress' và thuộc quyền xử lý của Assistant.",
        "basic": r"        \item Assistant chọn Task tương ứng." + "\n" + r"        \item Chọn chức năng 'Nộp kết quả (Submission)'." + "\n" + r"        \item Tải lên các file kết quả (Chỉ chấp nhận JPEG, PNG, PSD; dung lượng tối đa 20MB/file)." + "\n" + r"        \item Viết ghi chú đính kèm." + "\n" + r"        \item Nhấn 'Gửi'. Hệ thống lưu file lên Cloud Storage, chuyển trạng thái Task sang 'Reviewing' và gửi Notification cho Mangaka.",
        "alt": r"        \item \textbf{A1}: File sai định dạng hoặc quá dung lượng 20MB. Hệ thống từ chối tải lên, bôi đỏ lỗi và hướng dẫn Assistant nén file hoặc đổi định dạng.",
        "post": "Submission được ghi nhận an toàn, phiên bản (version) được cập nhật."
    },
    {
        "sub": r"\subsubsection{UC-21: Xem chi tiết Submission}\label{subsubsec:uc21_view_submission}",
        "id": "UC-21", "name": "Xem chi tiết Submission", "actor": "Mangaka, Tantou Editor", "label": "uc21",
        "desc": "Xem bản thảo chất lượng cao đã nộp để đưa ra nhận xét trực quan.",
        "pre": "Tồn tại ít nhất 1 Submission và tài khoản có quyền truy cập dữ liệu của Task.",
        "basic": r"        \item Người dùng nhấn vào link trong thông báo hoặc mở chi tiết Task." + "\n" + r"        \item Hệ thống render file bản thảo (nếu là PSD sẽ render bản preview) tích hợp công cụ thu phóng ảnh." + "\n" + r"        \item Người dùng xem nội dung hình ảnh và đọc các ghi chú đi kèm.",
        "alt": r"        \item \textbf{A1}: File bị lỗi corrupt (hỏng) không thể render. Hệ thống thông báo lỗi hiển thị và cung cấp nút 'Tải file gốc về máy' để xem cục bộ.",
        "post": "Người dùng tiếp nhận đầy đủ kết quả công việc của Assistant."
    },
    {
        "sub": r"\subsubsection{UC-22: Xem lịch sử Submission}\label{subsubsec:uc22_submission_history}",
        "id": "UC-22", "name": "Xem lịch sử Submission", "actor": "Tất cả", "label": "uc22",
        "desc": "Truy xuất và xem lại toàn bộ các lần nộp bản thảo (phiên bản) trước đó của một Task/Page.",
        "pre": "Task/Page có từ 1 lần Submission trở lên.",
        "basic": r"        \item Người dùng chọn 'Lịch sử nộp bài' (Version History)." + "\n" + r"        \item Hệ thống truy xuất Database, liệt kê danh sách các version theo dòng thời gian (Timeline)." + "\n" + r"        \item Người dùng có thể nhấn vào từng version để xem bản lưu trước đó.",
        "alt": r"        \item \textbf{A1}: Phiên bản cũ đã bị xóa khỏi lưu trữ để tiết kiệm dung lượng. Hệ thống hiển thị 'Phiên bản này đã lưu trữ ngoại tuyến (Archived)'.",
        "post": "Tính minh bạch của quá trình chỉnh sửa bản thảo được đảm bảo."
    },
    {
        "sec": r"\subsection{Quản lý Review (Review Management)}\label{subsec:srs_review_mgmt}",
        "sub": r"\subsubsection{UC-23: Tạo Review cho Submission}\label{subsubsec:uc23_create_review}",
        "id": "UC-23", "name": "Tạo Review cho Submission", "actor": "Tantou Editor, Mangaka", "label": "uc23",
        "desc": "Thêm nhận xét, vẽ khoanh vùng lỗi trực tiếp lên ảnh bản thảo và yêu cầu chỉnh sửa.",
        "pre": "Đang xem giao diện chi tiết một Submission chưa được Approve.",
        "basic": r"        \item Người dùng chọn công cụ vẽ (highlight, khoanh vùng, bút đỏ) trên trình duyệt." + "\n" + r"        \item Vẽ đánh dấu trực tiếp lên các điểm cần sửa trên file ảnh." + "\n" + r"        \item Nhập comment nhận xét (văn bản) cho từng vùng đánh dấu." + "\n" + r"        \item Chọn 'Approve' (Chấp nhận) hoặc 'Request Changes' (Yêu cầu sửa)." + "\n" + r"        \item Hệ thống lưu tọa độ đánh dấu, nội dung text và gửi email/push notification cho tác giả/trợ lý.",
        "alt": r"        \item \textbf{A1}: Mất kết nối mạng khi đang khoanh vùng lỗi. Hệ thống tự động lưu nháp (Auto-save) vào LocalStorage của trình duyệt và cảnh báo 'Đang ngoại tuyến'.",
        "post": "Tọa độ Annotation (được lưu trữ tại cột \\texttt{annotations} trong cơ sở dữ liệu) và kết quả Review được lưu trữ vĩnh viễn, trạng thái Task thay đổi tương ứng."
    },
    {
        "sub": r"\subsubsection{UC-24: Xem chi tiết Review}\label{subsubsec:uc24_view_review}",
        "id": "UC-24", "name": "Xem chi tiết Review", "actor": "Assistant, Mangaka", "label": "uc24",
        "desc": "Người thực hiện công việc xem lại các điểm cần sửa chữa do Editor/Mangaka đánh dấu.",
        "pre": "Submission đã được Review và có ít nhất 1 nhận xét hoặc đánh dấu.",
        "basic": r"        \item Người dùng mở Submission đã bị gắn cờ 'Request Changes'." + "\n" + r"        \item Hệ thống tải tọa độ Annotation, hiển thị ảnh gốc xếp chồng (overlay) các vùng khoanh đỏ của reviewer." + "\n" + r"        \item Người dùng trỏ chuột (hover) vào vùng khoanh đỏ để đọc bình luận chi tiết tương ứng.",
        "alt": r"        \item \textbf{A1}: Trình duyệt không hỗ trợ Canvas render. Hệ thống tự động chuyển sang chế độ hiển thị danh sách nhận xét dạng text thuần túy.",
        "post": "Người thực hiện định vị chính xác vị trí lỗi cần khắc phục trên bức tranh."
    },
    {
        "sub": r"\subsubsection{UC-25: Phản hồi yêu cầu chỉnh sửa}\label{subsubsec:uc25_respond_review}",
        "id": "UC-25", "name": "Phản hồi yêu cầu chỉnh sửa", "actor": "Assistant, Mangaka", "label": "uc25",
        "desc": "Gửi lại file mới (Revision) sau khi đã sửa lỗi theo yêu cầu của Review.",
        "pre": "Tồn tại một Review ở trạng thái 'Request Changes' yêu cầu người dùng phải hành động.",
        "basic": r"        \item Assistant hoàn tất sửa lỗi trên phần mềm vẽ cục bộ." + "\n" + r"        \item Vào mục Review, chọn chức năng 'Nộp bản sửa' (Submit Revision)." + "\n" + r"        \item Tải file bản vá (patch) lên và tích vào các checkbox đánh dấu 'Đã sửa' cho từng comment của Reviewer." + "\n" + r"        \item Hệ thống tăng version của Submission, liên kết bản mới này với Review cũ và thông báo cho Reviewer kiểm tra lại.",
        "alt": r"        \item \textbf{A1}: Thuật toán Hash phát hiện file gửi lên giống hệt file cũ. Hệ thống từ chối tải lên và yêu cầu 'Vui lòng nộp file đã có chỉnh sửa'.",
        "post": "Chu trình duyệt bài lặp lại, đảm bảo kiểm soát chất lượng."
    },
    {
        "sec": r"\subsection{Xét duyệt \& Xuất bản (Approval \& Publishing)}\label{subsec:srs_publishing_mgmt}",
        "sub": r"\subsubsection{UC-26: Xét duyệt Series mới}\label{subsubsec:uc26_approve_series}",
        "id": "UC-26", "name": "Xét duyệt Series mới", "actor": "Editorial Board", "label": "uc26",
        "desc": "Đánh giá, bỏ phiếu và phê duyệt một Series mới (Pilot/One-shot) được Mangaka đề xuất.",
        "pre": "Tài khoản thuộc nhóm Editorial Board, tồn tại Series ở trạng thái 'Pending Approval'.",
        "basic": r"        \item Hội đồng xem xét tài liệu Pitching, Kịch bản One-shot của Series." + "\n" + r"        \item Tổ chức tính năng họp bàn hoặc bỏ phiếu nội bộ trên hệ thống." + "\n" + r"        \item Tổng biên tập (đại diện Hội đồng) chọn 'Approve' (Duyệt) hoặc 'Reject' (Từ chối)." + "\n" + r"        \item Hệ thống cập nhật trạng thái Series (Thành 'Ongoing' nếu duyệt) và gửi thư phản hồi tự động.",
        "alt": r"        \item \textbf{A1}: Ý tưởng tốt nhưng cần sửa lại kịch bản. Hội đồng chọn 'Needs Revision', điền yêu cầu sửa và trả lại cho tác giả.",
        "post": "Series có trạng thái pháp lý và hoạt động chính thức trên nền tảng."
    },
    {
        "sub": r"\subsubsection{UC-27: Xuất bản Chapter}\label{subsubsec:uc27_publish_chapter}",
        "id": "UC-27", "name": "Xuất bản Chapter", "actor": "Editorial Board", "label": "uc27",
        "desc": "Phát hành Chapter ra công chúng, website hoặc nền tảng đọc trực tuyến.",
        "pre": "Chapter đã hoàn thiện 100\%, hoàn tất Review và được Tantou Editor thông qua (Approved).",
        "basic": r"        \item Hội đồng kiểm tra chất lượng file lần cuối." + "\n" + r"        \item Chọn Chapter, thiết lập ngày giờ phát hành (Timezone mặc định)." + "\n" + r"        \item Nhấn 'Publish'." + "\n" + r"        \item Hệ thống đổi trạng thái Chapter thành 'Published', đóng dấu Watermark chống vi phạm bản quyền và phân phối tới Database đọc truyện.",
        "alt": r"        \item \textbf{A1}: Thiết lập lịch phát hành tự động (Scheduled Publish). Hệ thống sẽ chuyển trạng thái 'Scheduled' và chờ Trigger tự động đổi thành 'Published' khi đến giờ G.",
        "post": "Chapter được phát hành chính thức, người dùng không thể sửa đổi nội dung cốt lõi nữa."
    },
    {
        "sub": r"\subsubsection{UC-28: Quyết định ngừng phát hành}\label{subsubsec:uc28_cease_publish}",
        "id": "UC-28", "name": "Quyết định ngừng phát hành", "actor": "Editorial Board", "label": "uc28",
        "desc": "Đình chỉ (hiatus) hoặc kết thúc (axe) một Series do thành tích xếp hạng kém hoặc lý do cá nhân của tác giả.",
        "pre": "Series đang ở trạng thái phát hành 'Ongoing'.",
        "basic": r"        \item Hội đồng chọn Series cần xử lý." + "\n" + r"        \item Chọn 'Change Status' $\rightarrow$ 'Cancelled' (Hủy bỏ) hoặc 'Hiatus' (Tạm ngưng)." + "\n" + r"        \item Nhập lý do (bắt buộc để lưu hồ sơ)." + "\n" + r"        \item Hệ thống lưu trạng thái, tự động đóng băng toàn bộ các Task/Chapter đang mở thuộc Series và thông báo cho toàn đội ngũ sản xuất.",
        "alt": r"        \item \textbf{A1}: Tạm ngưng có thời hạn vì lý do sức khỏe. Người dùng thiết lập thêm 'Ngày dự kiến mở lại', hệ thống sẽ gửi nhắc nhở khi sắp đến hạn.",
        "post": "Series bị dừng vô thời hạn hoặc có thời hạn, quy trình sản xuất tạm khóa."
    },
    {
        "sec": r"\subsection{Quản lý Xếp hạng (Ranking Management)}\label{subsec:srs_ranking_mgmt}",
        "sub": r"\subsubsection{UC-29: Nhập dữ liệu bình chọn}\label{subsubsec:uc29_input_votes}",
        "id": "UC-29", "name": "Nhập dữ liệu bình chọn", "actor": "Admin, Editorial Board", "label": "uc29",
        "desc": "Nhập dữ liệu phiếu bầu (vote) của độc giả từ tạp chí giấy hoặc API hệ thống ngoài.",
        "pre": "Tài khoản có quyền Admin/Editor. Đã có dữ liệu thô từ bộ phận khảo sát độc giả.",
        "basic": r"        \item Người dùng vào module 'Quản lý xếp hạng'." + "\n" + r"        \item Chọn Kỳ phát hành tạp chí (Issue Number)." + "\n" + r"        \item Nhập thủ công số phiếu bầu hoặc điểm số cho từng Series đang phát hành." + "\n" + r"        \item Nhấn 'Tính toán \& Lưu'." + "\n" + r"        \item Hệ thống cập nhật bảng xếp hạng cho kỳ đó vào Database.",
        "alt": r"        \item \textbf{A1}: Import hàng loạt từ file Excel (.xlsx). Hệ thống tự động đọc file, ánh xạ cột dữ liệu và tính toán thứ hạng giảm dần lỗi nhập tay.",
        "post": "Bảng xếp hạng của kỳ phát hành được cập nhật và đóng băng chỉnh sửa."
    },
    {
        "sub": r"\subsubsection{UC-30: Xem bảng xếp hạng}\label{subsubsec:uc30_view_ranking}",
        "id": "UC-30", "name": "Xem bảng xếp hạng", "actor": "Tất cả", "label": "uc30",
        "desc": "Xem thứ hạng hiện tại của các Series trên tạp chí để đánh giá mức độ phổ biến.",
        "pre": "Người dùng đã đăng nhập hệ thống nội bộ.",
        "basic": r"        \item Người dùng chọn menu 'Bảng xếp hạng'." + "\n" + r"        \item Hệ thống truy xuất và hiển thị danh sách Series sắp xếp theo thứ hạng của kỳ mới nhất." + "\n" + r"        \item Giao diện hiển thị mũi tên xanh/đỏ biểu thị xu hướng (tăng/giảm hạng) so với kỳ phát hành liền trước.",
        "alt": r"        \item \textbf{A1}: Chưa có dữ liệu bình chọn của kỳ hiện tại. Hệ thống hiển thị bảng xếp hạng của kỳ gần nhất kèm dòng thông báo 'Dữ liệu tuần này đang được cập nhật'.",
        "post": "Mangaka và Editor nắm được tình hình cạnh tranh và áp lực thị hiếu."
    },
    {
        "sub": r"\subsubsection{UC-31: Xem lịch sử xếp hạng}\label{subsubsec:uc31_ranking_history}",
        "id": "UC-31", "name": "Xem lịch sử xếp hạng", "actor": "Tất cả", "label": "uc31",
        "desc": "Xem biểu đồ biến động thứ hạng (Ranking Trend) của một Series cụ thể qua thời gian.",
        "pre": "Người dùng đang xem Dashboard chi tiết của một Series.",
        "basic": r"        \item Người dùng chuyển sang tab 'Lịch sử xếp hạng' (Ranking History) của Series." + "\n" + r"        \item Hệ thống vẽ biểu đồ đường (Line chart) thể hiện thứ hạng qua các tuần/kỳ." + "\n" + r"        \item Người dùng trỏ chuột (hover) vào từng giao điểm để xem chính xác số phiếu bầu và thứ hạng.",
        "alt": r"        \item \textbf{A1}: Series mới phát hành được 1 kỳ. Biểu đồ chỉ hiển thị dạng 1 điểm (Dot) và thông báo 'Chưa đủ dữ liệu vẽ xu hướng'.",
        "post": "Cung cấp phân tích trực quan về vòng đời và mức độ yêu thích của tác phẩm."
    },
    {
        "sec": r"\subsection{Quản lý Thông báo (Notification Management)}\label{subsec:srs_notification_mgmt}",
        "sub": r"\subsubsection{UC-32: Xem danh sách thông báo}\label{subsubsec:uc32_view_notifications}",
        "id": "UC-32", "name": "Xem danh sách thông báo", "actor": "Tất cả", "label": "uc32",
        "desc": "Xem các thông báo hệ thống gửi đến tài khoản (nhắc nhở deadline, có task mới, review mới).",
        "pre": "Người dùng đã đăng nhập thành công.",
        "basic": r"        \item Người dùng nhấn vào biểu tượng 'Chuông thông báo' trên góc phải màn hình." + "\n" + r"        \item Hệ thống truy vấn (Real-time Socket) và xổ xuống menu (dropdown) chứa 5-10 thông báo mới nhất." + "\n" + r"        \item Người dùng có thể bấm 'Xem tất cả' để điều hướng sang trang quản lý thông báo chi tiết.",
        "alt": r"        \item \textbf{A1}: Không có thông báo nào trong cơ sở dữ liệu. Menu thả xuống hiển thị ảnh minh họa (empty state) 'Bạn đã xem hết thông báo mới'.",
        "post": "Người dùng nắm bắt được các sự kiện quan trọng cần xử lý gấp."
    },
    {
        "sub": r"\subsubsection{UC-33: Đánh dấu đã đọc}\label{subsubsec:uc33_read_notification}",
        "id": "UC-33", "name": "Đánh dấu đã đọc", "actor": "Tất cả", "label": "uc33",
        "desc": "Đánh dấu một hoặc toàn bộ thông báo là đã xem để xóa huy hiệu (badge) báo hiệu chưa đọc.",
        "pre": "Có ít nhất 1 thông báo ở trạng thái chưa đọc (unread).",
        "basic": r"        \item Người dùng bấm vào một thông báo cụ thể (Hệ thống tự động kích hoạt chuyển trạng thái thành đã đọc)." + "\n" + r"        \item Hoặc người dùng bấm nút 'Đánh dấu tất cả đã đọc' (Mark all as read)." + "\n" + r"        \item Hệ thống cập nhật trường trạng thái trong DB." + "\n" + r"        \item Biểu tượng số lượng thông báo mới (đỏ) trên chuông giảm đi tương ứng hoặc biến mất.",
        "alt": r"        \item \textbf{A1}: Quá trình cập nhật DB thất bại do lỗi máy chủ. UI tự động khôi phục lại trạng thái chưa đọc và hiển thị toast 'Có lỗi xảy ra, thử lại sau'.",
        "post": "Giải phóng người dùng khỏi các nhắc nhở không còn cần thiết."
    }
]

out = []
for uc in ucs:
    if "sec" in uc:
        out.append(uc["sec"] + "\n")
    out.append(uc["sub"] + "\n")
    
    uc_text = TEMPLATE
    for key, value in uc.items():
        uc_text = uc_text.replace("[[" + key + "]]", value)
    
    out.append(uc_text + "\n")

with open("chapters/03_3_srs_func_2.tex", "w", encoding="utf-8") as f:
    f.write("".join(out))
