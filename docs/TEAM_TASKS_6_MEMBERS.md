# Phân chia nhiệm vụ chi tiết cho nhóm 6 người

> Mục tiêu: mỗi người có ownership rõ ràng theo đúng cấu trúc `src/`, và ai cũng phải trực tiếp tham gia xử lý đề tài, không ai chỉ làm việc hành chính.

## Thành viên 1 - Project Lead / Integration
**Phạm vi ownership**
- `src/app/main.py`
- Điều phối giữa `presentation`, `application`, `cv_pipeline`, `infrastructure`

**Nhiệm vụ chính**
- Chốt roadmap, milestone và thứ tự tích hợp.
- Review PR, merge nhánh, giữ codebase nhất quán.
- Xác nhận luồng chạy end-to-end từ video input đến kết quả slot.

**Deliverables**
- Kế hoạch sprint theo tuần.
- Bản tích hợp end-to-end chạy được.
- Checklist demo cuối kỳ.

## Thành viên 2 - Presentation / UI Flow
**Phạm vi ownership**
- `src/presentation/video_controller.py`
- Phần hiển thị, nhận nguồn video, overlay kết quả

**Nhiệm vụ chính**
- Hoàn thiện luồng đọc camera/video file.
- Hiển thị trạng thái occupancy, số slot trống/đầy.
- Chuẩn hóa trải nghiệm chạy demo trên máy giảng viên.

**Deliverables**
- Controller hiển thị ổn định.
- Overlay trạng thái và summary trên frame.
- Hướng dẫn thao tác chạy demo.

## Thành viên 3 - CV Pipeline Core
**Phạm vi ownership**
- `src/cv_pipeline/preprocessing.py`
- `src/cv_pipeline/background_subtraction.py`
- `src/cv_pipeline/thresholding.py`
- `src/cv_pipeline/morphology.py`

**Nhiệm vụ chính**
- Tinh chỉnh preprocessing và background subtraction.
- Cải thiện threshold/morphology cho từng video/camera.
- Đo tốc độ xử lý và độ ổn định theo frame.

**Deliverables**
- Pipeline CV baseline hoàn chỉnh.
- Bộ tham số cấu hình đề xuất.
- Báo cáo FPS/độ ổn định theo video test.

## Thành viên 4 - Slot Extraction / Classification
**Phạm vi ownership**
- `src/cv_pipeline/contour_detection.py`
- `src/cv_pipeline/slot_extraction.py`
- `src/cv_pipeline/classifier.py`
- `config/slots.json`

**Nhiệm vụ chính**
- Tách ROI từng slot từ polygon.
- Đưa ra rule classifier cho occupied/free/unknown.
- Chuẩn hóa format slot data để các layer khác dùng thống nhất.

**Deliverables**
- Module trích xuất slot theo polygon.
- Logic phân loại trạng thái slot.
- File cấu hình slot mẫu đã chuẩn hóa.

## Thành viên 5 - Infrastructure / Data
**Phạm vi ownership**
- `src/infrastructure/opencv/video_reader.py`
- `src/infrastructure/repositories/json_slot_repository.py`
- `data/`
- `models/`

**Nhiệm vụ chính**
- Duy trì adapter OpenCV và repository JSON.
- Chuẩn bị đường dẫn dữ liệu video/dataset/model.
- Lên kế hoạch nâng cấp từ JSON sang storage bền vững hơn nếu cần.

**Deliverables**
- Video reader adapter ổn định.
- Repository đọc/ghi slot chuẩn.
- Cấu trúc dữ liệu và model placeholder rõ ràng.

## Thành viên 6 - QA / Validation / Demo Support
**Phạm vi ownership**
- `README.md`
- `docs/ARCHITECTURE.md`
- `docs/TODO.md`
- `docs/TEAM_TASKS_6_MEMBERS.md`
- Test video mẫu end-to-end
- Kiểm tra output của pipeline và dữ liệu slot

**Nhiệm vụ chính**
- Chạy kiểm thử end-to-end với video mẫu để xác nhận pipeline hoạt động đúng.
- Kiểm tra input/output của `config/slots.json`, dữ liệu video và kết quả occupancy.
- Viết test checklist theo từng layer và ghi nhận bug/edge case.
- Hỗ trợ validate kết quả detector, smoothing và overlay trước khi demo.
- Chuẩn hóa tài liệu cài đặt, chạy, demo như phần hỗ trợ cho việc bàn giao.

**Deliverables**
- Bộ test end-to-end với video mẫu và kết quả ghi nhận.
- Checklist test theo từng milestone.
- Biên bản tổng hợp lỗi, rủi ro và dữ liệu cần chỉnh.
- Tài liệu dự án hoàn chỉnh.

---

## Cơ chế phối hợp
- Daily sync 15 phút.
- Mỗi tuần 1 nhánh tích hợp ổn định.
- PR bắt buộc có ít nhất 1 reviewer và kiểm tra lỗi cơ bản pass.
- Nếu blocker kéo dài quá 24 giờ, báo ngay cho Thành viên 1 để chốt hướng xử lý.
