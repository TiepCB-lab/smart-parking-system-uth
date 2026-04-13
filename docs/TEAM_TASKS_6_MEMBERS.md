# BẢNG PHÂN CÔNG NHIỆM VỤ CHI TIẾT CHO NHÓM 6 THÀNH VIÊN

> Phạm vi dự án: hệ thống Smart Parking theo cấu trúc 3-layer + CV pipeline trong `src/`.
> Mục tiêu phân công: 100% thành viên tham gia xử lý kỹ thuật trực tiếp (code, test, tích hợp), không có vai trò chỉ làm tài liệu.

## 1) Tổng quan phân vai theo cấu trúc project

| Thành viên | Vai trò chính | Ownership module/files chính | Đầu ra chính |
|---|---|---|---|
| TV1 | Lead + Integration + Architecture Guard | `src/app/main.py`, `src/application/use_cases/process_video.py`, `src/application/use_cases/process_multi_camera.py`, `src/domain/interfaces.py` | Luồng end-to-end ổn định, tích hợp đa camera, quy trình merge/release |
| TV2 | Presentation + UX Demo | `src/presentation/video_controller.py`, `src/presentation/multi_camera_controller.py` | Giao diện/chạy demo video và multi-camera rõ ràng, overlay đầy đủ |
| TV3 | CV Core (Preprocess + Foreground) | `src/cv_pipeline/preprocessing.py`, `src/cv_pipeline/background_subtraction.py`, `src/cv_pipeline/thresholding.py`, `src/cv_pipeline/morphology.py` | Detector baseline sử dụng background subtraction, thông số tối ưu |
| TV4 | Slot Logic (Contour/ROI/Classifier) | `src/cv_pipeline/contour_detection.py`, `src/cv_pipeline/slot_extraction.py`, `src/cv_pipeline/classifier.py`, `config/slots.example.json` | Trích xuất slot chính xác, phân loại occupied/free/unknown, smoothing |
| TV5 | Infrastructure + Data + Repository | `src/infrastructure/opencv/video_reader.py`, `src/infrastructure/repositories/json_slot_repository.py`, `data/`, `models/`, `config/slots.example.json` | Adapter đọc video/repository ổn định, bộ dữ liệu/chuẩn hóa config |
| TV6 | QA + Evaluation + Automation | `src/evaluation/evaluator.py`, test scripts benchmark/end-to-end, regression scenarios | Bộ test tự động, kết quả benchmark, bug reproduction packs |

## 2) Bảng nhiệm vụ chi tiết từng thành viên

## Thành viên 1 - Lead/Integration (TV1)

**Mục tiêu**
- Đảm bảo các layer kết nối đúng chuẩn: Presentation -> Application -> Domain -> Infrastructure/CV pipeline.
- Chốt mọi hợp đồng dữ liệu và luồng xử lý chính.

**Nhiệm vụ kỹ thuật chi tiết**
1. Chuẩn hóa use-case xử lý 1 camera và nhiều camera.
2. Định nghĩa rõ interface giữa `application` và `cv_pipeline` (input frame, output kết quả slot).
3. Đảm bảo `main.py` có 2 mode chạy: single-video và multi-camera.
4. Viết luồng xử lý lỗi tổng quan (video không mở được, file slot không hợp lệ, camera disconnect).
5. Thiết kế cấu hình runtime có thể truyền qua argument hoặc file config.
6. Điều phối merge theo nhánh tích hợp từng tuần, giải quyết xung đột module.

**Deliverables bắt buộc**
- 1 phiên bản chạy thông suốt từ `python -m src.app.main` đến kết quả occupancy.
- 1 bộ integration test scenarios cho luồng single và multi-camera.

**KPI/DoD của TV1**
- Chạy ổn định với ít nhất 2 video mẫu khác nhau.
- Không còn lỗi import vòng lặp giữa các layer.
- Tất cả PR lớn đều có tiêu chí test/kiểm tra rõ ràng.

---

## Thành viên 2 - Presentation/Controller (TV2)

**Mục tiêu**
- Biến kết quả CV thành giao diện quan sát để demo được ngay.

**Nhiệm vụ kỹ thuật chi tiết**
1. Hoàn thiện `video_controller.py`:
	- Chọn nguồn video, play/pause, frame stepping cơ bản (nếu cần).
	- Vẽ overlay polygon slot, id slot, màu occupied/free.
	- Hiển thị thống kê tổng số slot trống/đã có xe theo frame.
2. Hoàn thiện `multi_camera_controller.py`:
	- Sắp xếp layout nhiều camera trong một cửa sổ.
	- Hiển thị thống kê từng camera và tổng hợp.
3. Đồng bộ style output để dễ quan sát khi demo (font/màu/legend nhất quán).
4. Tích hợp callback nhận kết quả từ application layer, không chèn logic CV vào presentation.
5. Xử lý trường hợp UI không nhận được frame/kết quả (fallback message).

**Deliverables bắt buộc**
- Giao diện có overlay rõ ràng cho single-camera.
- Giao diện cơ bản cho multi-camera (tối thiểu 2 nguồn).
- 1 bộ config chạy demo (tham số input/ngưỡng/màu hiển thị) dùng lại được.

**KPI/DoD của TV2**
- Tốc độ hiển thị không giật mạnh trên máy nhóm dùng demo.
- Màu sắc occupied/free không bị nhầm trong điều kiện ánh sáng trung bình.
- Có screenshot/clip ngắn cho 2 kịch bản: single và multi-camera.

---

## Thành viên 3 - CV Core Baseline (TV3)

**Mục tiêu**
- Tạo baseline detector ổn định dựa trên preprocessing + background subtraction.

**Nhiệm vụ kỹ thuật chi tiết**
1. Trong `preprocessing.py`:
	- Chuẩn hóa resize, grayscale, blur (median/gaussian) có tham số.
2. Trong `background_subtraction.py`:
	- Thử nghiệm MOG2/KNN.
	- Chuẩn hóa ngưỡng foreground ratio cho từng slot.
3. Trong `thresholding.py` và `morphology.py`:
	- Bộ lọc nhiễu (opening/closing), loại bỏ đốm nhỏ.
	- Tạo helper để thử nghiệm nhanh bộ tham số.
4. Đưa ra bộ tham số baseline theo từng điều kiện:
	- Ban ngày, ban tối, camera rung nhẹ.
5. Đánh dấu các case detector yếu và đề xuất hướng nâng cấp (YOLO segmentation/custom model).

**Deliverables bắt buộc**
- Baseline detector có hàm chạy và trả kết quả nhất quán.
- Bảng tham số khuyến nghị theo ít nhất 3 điều kiện video.
- Script benchmark FPS/latency cho baseline detector.

**KPI/DoD của TV3**
- Pipeline core có thể xử lý liên tục trên video mẫu mà không vỡ frame.
- Kết quả foreground mask đủ sạch để TV4 classifier sử dụng.
- Các tham số được đưa vào config/có constant rõ ràng, không hard-code rải rác.

---

## Thành viên 4 - Slot Extraction + Classification (TV4)

**Mục tiêu**
- Biến mask/contour thành trạng thái từng slot để sử dụng trực tiếp trong dashboard/demo.

**Nhiệm vụ kỹ thuật chi tiết**
1. `contour_detection.py`:
	- Tách contour vùng xe/noise và đánh dấu độ tin cậy cơ bản.
2. `slot_extraction.py`:
	- Cắt ROI theo polygon slot từ config.
	- Đảm bảo đúng hệ tọa độ khi frame đã resize.
3. `classifier.py`:
	- Rule occupied/free dựa trên pixel ratio, contour area, và confidence.
	- Thêm trạng thái `unknown` khi kết quả không chắc chắn.
4. Xây cơ chế smoothing/debounce theo N frame để giảm nháy trạng thái.
5. Chuẩn hóa schema slot:
	- `slot_id`, `polygon`, `camera_id`, `status`, `confidence`, `timestamp`.

**Deliverables bắt buộc**
- Module classifier trả về danh sách slot có status + confidence.
- Cơ chế debounce hoạt động trên ít nhất 1 video nhiễu.
- File mẫu `config/slots.example.json` có schema rõ ràng, để sinh `config/slots.json`.

**KPI/DoD của TV4**
- Trạng thái slot không bị đảo qua lại liên tục trong cảnh ổn định.
- Tỷ lệ slot không xác định (`unknown`) được giảm dần qua các sprint.
- Dữ liệu output slot được TV2/TV6 đọc và visual/evaluate trực tiếp.

---

## Thành viên 5 - Infrastructure + Data (TV5)

**Mục tiêu**
- Cung cấp hạ tầng đọc video, quản lý config slot, và dữ liệu test để nhóm làm việc trơn tru.

**Nhiệm vụ kỹ thuật chi tiết**
1. `video_reader.py`:
	- Wrapper OpenCV cho file video và stream camera.
	- Xử lý reconnect/cơ chế retry có giới hạn.
2. `json_slot_repository.py`:
	- Đọc/ghi slot config an toàn, validate schema.
	- Báo lỗi rõ ràng khi file sai format.
3. Quản lý thư mục `data/`:
	- Chuẩn hóa tên file video test, metadata cơ bản (fps, resolution, thời tiết).
	- Tách bộ dữ liệu train/val/test nếu phát triển model nâng cao.
4. Quản lý `models/`:
	- Đặt convention tên model + version.
	- Tạo placeholder/hướng dẫn lưu trữ model.
5. Đề xuất migration Data & API:
	- Phương án chuyển JSON -> SQLite/PostgreSQL.
	- Bộ schema occupancy history cho giai đoạn 3.

**Deliverables bắt buộc**
- Adapter đọc video sử dụng ổn định cho TV1/TV2.
- Repository config có validate schema cơ bản.
- Danh mục video benchmark với mô tả ngắn gọn.
- 1 prototype lưu occupancy history vào SQLite (minimal schema + ghi đọc cơ bản).

**KPI/DoD của TV5**
- Lỗi file/video không làm crash toàn bộ chương trình.
- Các file config mẫu đọc được ở mọi máy thành viên.
- Có ít nhất 3 video benchmark được đồng bộ cho nhóm.

---

## Thành viên 6 - QA + Evaluation + Automation (TV6)

**Mục tiêu**
- Đảm bảo kết quả có thể kiểm chứng được bằng test script, benchmark script và bộ testcase tái lập lỗi.

**Nhiệm vụ kỹ thuật chi tiết**
1. `src/evaluation/evaluator.py`:
	- Xây script tính các chỉ số cơ bản: accuracy/precision/recall theo slot nếu có nhãn.
	- Có mode so sánh output giữa các phiên bản detector.
2. Xây bộ regression tests:
	- Tự động chạy cho single-camera và multi-camera.
	- Lưu output theo format để so sánh giữa các lần run.
3. Test kịch bản end-to-end:
	- Chạy với single-camera và multi-camera.
	- Kiểm tra case mất kết nối camera, file slot lỗi, thay đổi ánh sáng.
4. Tạo bộ testcase tái lập lỗi (bug reproduction packs):
	- Mỗi bug có input, tham số, output mong đợi, output thực tế.
	- Đánh dấu bug theo mức độ nghiêm trọng để ưu tiên fix.
5. Chuẩn bị benchmark package cuối kỳ:
	- Script benchmark 5-7 phút cho kịch bản demo.
	- Bảng kết quả benchmark để đối chiếu trước/sau mỗi tối ưu.

**Deliverables bắt buộc**
- Bộ regression test script chạy được trên máy nhóm.
- Bộ benchmark script + output metrics lưu theo sprint.
- Bộ bug reproduction packs cho các lỗi critical/major.

**KPI/DoD của TV6**
- Mỗi sprint đều có kết quả regression pass/fail rõ ràng.
- Các bug critical đều có testcase tái lập được.
- Benchmark cho thấy xu hướng cải thiện hoặc cảnh báo suy giảm hiệu năng.

## 3) Kế hoạch theo giai đoạn (gắn với docs/TODO.md)

| Giai đoạn | Mục tiêu | TV chịu trách nhiệm chính | TV phối hợp |
|---|---|---|---|
| Giai đoạn 1 - Setup nền tảng | Chốt structure, config slot, convention code/branch | TV1, TV5 | TV6 |
| Giai đoạn 2 - CV Core | Baseline detector + classifier + smoothing | TV3, TV4 | TV1, TV6 |
| Giai đoạn 3 - Data/API | Chuẩn bị persistence và API readiness | TV5, TV1 | TV6 |
| Giai đoạn 4 - Dashboard/Demo | Multi-camera monitoring + script benchmark/demo | TV2, TV6 | TV1, TV3, TV4 |

## 4) Điểm bàn giao (handoff) bắt buộc

1. TV5 -> TV3/TV4:
	- Bàn giao video benchmark + config slot hợp lệ.
2. TV3 -> TV4:
	- Bàn giao foreground/mask output và thông số đã tối ưu.
3. TV4 -> TV2:
	- Bàn giao output status slot + confidence để vẽ overlay.
4. TV2 -> TV6:
	- Bàn giao kịch bản thao tác demo và output cần validate.
5. TV6 -> TV1:
	- Bàn giao báo cáo lỗi/rủi ro để chốt sprint và plan sprint tiếp.

## 5) Cơ chế làm việc và kiểm soát chất lượng

1. Nhánh làm việc:
	- Mỗi TV tạo nhánh theo module (`feature/tvX-module-name`).
2. Quy tắc PR:
	- Mỗi PR phải ghi rõ: mục tiêu, file ảnh hưởng, cách test, screenshot/log (nếu có).
3. Review:
	- Tối thiểu 1 reviewer, ưu tiên reviewer là TV có liên quan handoff.
4. Lịch đồng bộ:
	- Daily sync 15 phút (blocker, progress, kế hoạch 24h tới).
	- Sprint review hằng tuần (demo và retro ngắn).
5. Quản lý blocker:
	- Blocker > 24h phải escalate cho TV1 để đổi hướng kỹ thuật.
6. Quy tắc tài liệu (không giao riêng 1 người):
	- Mỗi TV cập nhật phần mô tả kỹ thuật liên quan ngay trong PR của mình.
	- TV nào code module nào thì cập nhật phần hướng dẫn module đó.

## 6) Tiêu chí hoàn thành toàn nhóm (Team DoD)

- Chạy được end-to-end trên ít nhất 1 kịch bản single-camera và 1 kịch bản multi-camera.
- Có kết quả occupancy và overlay rõ ràng theo từng slot.
- Có test checklist + báo cáo đánh giá mỗi sprint.
- Mỗi module chính đều có test hoặc script kiểm chứng tương ứng.
- Có kịch bản demo cuối kỳ và phương án dự phòng khi lỗi camera/video.
