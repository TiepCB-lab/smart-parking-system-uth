# Kiến trúc dự án (skeleton trước, code sau)

## Mục tiêu
- Dựng **khung 3-layer** rõ ràng để nhóm phát triển song song.
- Chỉ để TODO và stub cơ bản, **chưa triển khai hoàn thiện**.

## 3-layer đề xuất

### 1) Presentation Layer
- Chứa controller/CLI/UI để nhận input video.
- Không chứa thuật toán CV chi tiết.

### 2) Application Layer
- Chứa use-case điều phối luồng nghiệp vụ.
- Gọi detector và repository qua abstraction.

### 3) Domain Layer
- Chứa entity + interface cốt lõi.
- Không phụ thuộc OpenCV/DB/framework.

## Infrastructure Layer (adapter)
- OpenCV detector adapter.
- JSON/DB repository adapter.

## Quy tắc dependency
- Presentation -> Application -> Domain.
- Infrastructure implement interface trong Domain.
- Domain không import layer khác.

## Trạng thái hiện tại
- [x] Tạo cấu trúc thư mục.
- [x] Tạo file skeleton với TODO.
- [ ] Chưa hoàn thiện thuật toán detector.
- [ ] Chưa hoàn thiện repository và UI run loop.
