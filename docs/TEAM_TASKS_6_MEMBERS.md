# Phân chia nhiệm vụ chi tiết cho nhóm 6 người

> Mục tiêu: mỗi người có ownership rõ ràng + có phần backup chéo để không nghẽn tiến độ.

## Thành viên 1 - Project Lead / Integration
**Nhiệm vụ chính**
- Quản lý roadmap, milestone, sprint board.
- Chốt kiến trúc, review PR, merge nhánh.
- Tích hợp toàn hệ thống và chuẩn bị demo.

**Deliverables**
- Kế hoạch sprint theo tuần.
- Biên bản review kiến trúc + quyết định kỹ thuật.
- Bản demo tích hợp cuối kỳ.

## Thành viên 2 - CV Engineer (Baseline)
**Nhiệm vụ chính**
- Xây baseline detector bằng OpenCV (MOG2, morphology).
- Tinh chỉnh threshold theo từng camera.
- Đánh giá accuracy trên bộ video test.

**Deliverables**
- Module detector baseline.
- Báo cáo precision/recall cơ bản.

## Thành viên 3 - CV Engineer (Advanced Model)
**Nhiệm vụ chính**
- Nghiên cứu mô hình nâng cao (YOLO segmentation).
- So sánh với baseline về accuracy/FPS.
- Chuẩn bị pipeline inference tối ưu cho máy demo.

**Deliverables**
- Module detector nâng cao.
- Bảng benchmark so sánh baseline vs advanced.

## Thành viên 4 - Data/Backend Engineer
**Nhiệm vụ chính**
- Thiết kế schema dữ liệu slot + lịch sử occupancy.
- Xây repository layer (JSON -> DB).
- Xây API cho dashboard lấy dữ liệu realtime/lịch sử.

**Deliverables**
- Script migration + seed dữ liệu.
- API docs (OpenAPI/Swagger).

## Thành viên 5 - Frontend/Dashboard Engineer
**Nhiệm vụ chính**
- Xây dashboard hiển thị trạng thái bãi xe.
- Thiết kế UI: tổng chỗ trống, camera view, cảnh báo.
- Tối ưu refresh realtime (polling/websocket).

**Deliverables**
- Giao diện dashboard chạy được.
- Tài liệu thao tác cho giảng viên/demo.

## Thành viên 6 - QA/Documentation Engineer
**Nhiệm vụ chính**
- Viết test cases end-to-end.
- Chuẩn hóa tài liệu README, kiến trúc, hướng dẫn chạy.
- Quản lý checklist release/demo và rủi ro.

**Deliverables**
- Bộ test checklist + kết quả test.
- Tài liệu hoàn chỉnh cho cài đặt, chạy, demo.

---

## Cơ chế phối hợp (đề xuất)
- Daily sync 15 phút.
- Mỗi tuần 1 integration branch ổn định.
- Quy tắc PR: tối thiểu 1 reviewer + 1 lần chạy check pass.
- Khi blocker > 24h: escalate cho Project Lead.
