# TÀI LIỆU ĐẶC TẢ YÊU CẦU PHẦN MỀM (SRS) - CẬP NHẬT V2
**Dự án:** Hệ thống Quản lý Bãi đỗ xe Thông minh (Smart Parking System)
**Sinh viên thực hiện:** Ngô Châu Kiệt
**Học phần:** Xử lý Ảnh và Thị giác Máy tính (121036)

---

## 1. GIỚI THIỆU (INTRODUCTION)
[cite_start]Hệ thống được thiết kế để giải quyết vấn đề quản lý bãi đỗ xe thực tế bằng cách sử dụng camera quét ô trống theo thời gian thực và hỗ trợ điều hướng tài xế[cite: 14].

## 2. RÀNG BUỘC KỸ THUẬT (TECHNICAL CONSTRAINTS)
[cite_start]Theo yêu cầu của đề tài[cite: 13, 15, 18]:
- Áp dụng ít nhất **3 kỹ thuật** từ chương trình học (Chương 2, 3, 4, 5).
- [cite_start]Sử dụng ngôn ngữ **Python** và các thư viện chuẩn (OpenCV, NumPy)[cite: 26].
- [cite_start]Đánh giá trên **dữ liệu thực tế**, không dùng dữ liệu tổng hợp[cite: 16, 28].
- [cite_start]Minh bạch Pipeline: Không sử dụng API Deep Learning dạng "hộp đen" làm giải pháp duy nhất.

## 3. CHI TIẾT 3 KỸ THUẬT ÁP DỤNG (CORE TECHNIQUES)

### 3.1 Biến đổi phối cảnh (Perspective Transform) - Chương 3
- [cite_start]**Kỹ thuật:** Sử dụng ma trận biến đổi 3x3 để tạo góc nhìn Bird-eye view[cite: 20].
- **Mục đích:** Loại bỏ độ méo do góc quay nghiêng của camera giám sát. Việc đưa hình ảnh về góc nhìn thẳng đứng giúp các ô đỗ xe (ROI) có kích thước đồng nhất, hỗ trợ việc phân đoạn chính xác hơn.

### 3.2 Phân đoạn ảnh (Image Segmentation) - Chương 4
- [cite_start]**Kỹ thuật:** Trừ nền (Background Subtraction) sử dụng thuật toán MOG2 kết hợp phát hiện đường viền (Contour Detection)[cite: 20].
- **Mục đích:** Tách biệt các đối tượng chuyển động (xe cộ) khỏi nền tĩnh (mặt đường). Khi tỷ lệ pixel thuộc lớp tiền cảnh (foreground) trong một ô đỗ vượt quá ngưỡng quy định, hệ thống sẽ xác định trạng thái là "Occupied".

### 3.3 Xử lý và Lọc ảnh (Image Processing & Morphology) - Chương 2 & 4
- [cite_start]**Kỹ thuật:** Lọc Gaussian (Gaussian Blur) và các toán tử hình thái học (Morphological Operations: Opening & Closing)[cite: 20].
- **Mục đích:** - **Gaussian Blur:** Giảm nhiễu hạt và làm mịn ảnh trước khi đưa vào bộ trừ nền.
    - **Morphology:** Phép "Opening" loại bỏ các nhiễu nhỏ (noise); phép "Closing" giúp lấp đầy các khoảng trống bên trong vật thể (như kính xe) để tạo ra mặt nạ nhị phân liền mạch, giúp tính toán mật độ pixel chính xác.

## 4. YÊU CẦU CHỨC NĂNG (FUNCTIONAL REQUIREMENTS)
- [cite_start]**FR1:** Thiết lập tọa độ ô đỗ qua file `slots.json`[cite: 27].
- **FR2:** Nhận diện trạng thái Trống/Đầy thời gian thực.
- **FR3:** Mô phỏng đa camera cho bãi xe nhiều tầng.
- [cite_start]**FR4:** Đánh giá định lượng (Accuracy, Precision, Recall) dựa trên Ground Truth[cite: 42, 54].

## 5. ĐÁNH GIÁ ĐỊNH LƯỢNG
[cite_start]Hệ thống bắt buộc phải xuất ra các chỉ số[cite: 42]:
- **Accuracy:** Độ chính xác tổng thể.
- **Precision:** Tỷ lệ dự đoán "Có xe" là chính xác.
- **Recall:** Khả năng phát hiện đúng tất cả các xe đang đỗ.