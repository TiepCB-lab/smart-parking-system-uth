# TODO tổng thể dự án Smart Parking (phiên bản khung)

## Giai đoạn 1 - Setup nền tảng
- [ ] Chuẩn hóa cấu trúc thư mục theo 3-layer.
- [ ] Chốt format file `config/slots.json`.
- [ ] Thiết lập lint/format (`ruff`, `black`).
- [ ] Thiết lập convention commit + branch.

## Giai đoạn 2 - Computer Vision core
- [ ] Tool annotate polygon slot từ ảnh/video.
- [ ] Baseline detector (Background Subtraction).
- [ ] Detector nâng cao (YOLO segmentation / custom model).
- [ ] Cơ chế smoothing trạng thái (debounce theo N frame).

## Giai đoạn 3 - Data & API
- [ ] Chuyển từ JSON sang SQLite/PostgreSQL.
- [ ] API trả trạng thái realtime (FastAPI).
- [ ] Log lịch sử occupancy theo thời gian.

## Giai đoạn 4 - Dashboard & Demo
- [ ] Dashboard hiển thị số chỗ trống.
- [ ] Trang giám sát nhiều camera.
- [ ] Kịch bản demo cuối kỳ + script benchmark.

## Definition of Done (gợi ý)
- [ ] Chạy được end-to-end với ít nhất 1 video mẫu.
- [ ] Độ chính xác occupancy đạt mục tiêu nhóm đặt ra.
- [ ] Có tài liệu hướng dẫn cài đặt/chạy đầy đủ.
