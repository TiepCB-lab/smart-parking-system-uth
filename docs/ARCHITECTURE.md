# Kiến trúc dự án

## Mục tiêu
- Dựng **khung 3-layer** rõ ràng để nhóm phát triển song song.
- Pipeline CV được tách thành các bước nhỏ trong `src/cv_pipeline`.

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

## CV Pipeline
- `preprocessing`: chuyển ảnh sang grayscale và làm mờ.
- `background_subtraction`: tạo foreground mask và suy luận trạng thái slot.
- `thresholding`, `morphology`, `contour_detection`, `slot_extraction`, `classifier`: các bước xử lý trung gian.

## Quy tắc dependency
- Presentation -> Application -> Domain.
- Infrastructure implement interface trong Domain.
- Domain không import layer khác.

## Trạng thái hiện tại
- [x] Tạo cấu trúc thư mục.
- [x] Tạo file skeleton với TODO.
- [x] Tách pipeline CV thành các module riêng.
- [x] Nối entrypoint, video reader và JSON repository.
- [ ] Chưa hoàn thiện thuật toán detector nâng cao và UI overlay.
