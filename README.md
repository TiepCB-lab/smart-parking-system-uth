# smart-parking-system-uth
Phát hiện và giám sát trạng thái chỗ đậu xe từ video bằng Python + OpenCV.

> ⚠️ Hiện tại repository này đang ở mức **khung dự án (skeleton)**: chỉ có cấu trúc + TODO list, chưa triển khai hoàn thiện logic trong bất kỳ module nào.

## 1) Mục tiêu đồ án
- Xây dựng hệ thống nhận diện chỗ đậu còn trống/đã có xe từ video camera.
- Hiển thị trạng thái trực quan và có thể mở rộng thành dashboard/API.

## 2) Kiến trúc đề xuất
Dùng mô hình **3-layer** với trung tâm xử lý ở `cv_pipeline`:
- `presentation`: nhận input/hiển thị.
- `application`: use-case điều phối nghiệp vụ.
- `domain`: entity + interface lõi.
- `cv_pipeline`: preprocessing, background subtraction, thresholding, morphology, contour, extraction, classifier.
- `infrastructure`: adapter cho OpenCV, JSON/DB.

Xem chi tiết tại [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## 3) Cấu trúc thư mục
```text
src/
├── app/
│   └── main.py
├── presentation/
│   └── video_controller.py
├── application/
│   └── use_cases/
│       └── process_video.py
├── domain/
│   ├── entities.py
│   └── interfaces.py
├── cv_pipeline/
│   ├── preprocessing.py
│   ├── background_subtraction.py
│   ├── thresholding.py
│   ├── morphology.py
│   ├── contour_detection.py
│   ├── slot_extraction.py
│   └── classifier.py
├── infrastructure/
│   ├── opencv/
│   │   └── video_reader.py
│   └── repositories/
│       └── json_slot_repository.py
├── data/
│   ├── videos/
│   └── dataset/
└── models/
    └── parking_model.pkl

config/
└── slots.json

docs/
├── ARCHITECTURE.md
├── TODO.md
└── TEAM_TASKS_6_MEMBERS.md
```

## 4) Hướng dẫn cài đặt
### Yêu cầu
- Python 3.10+

### Cài thư viện cơ bản
```bash
pip install opencv-python numpy
```

### Cấu hình slot mặc định
`config/slots.json` đã có sẵn để chạy ngay, `config/slots.example.json` dùng làm mẫu.

## 5) Cách chạy dự án (chế độ skeleton)
```bash
python -m src.app.main
```

Kết quả hiện tại: project đã được tái cấu trúc theo cây thư mục mới, pipeline CV được tách module rõ ràng và entrypoint đã nối đủ các adapter chính.

## 6) Tài liệu quản lý công việc
- TODO tổng thể: `docs/TODO.md`
- Phân chia nhiệm vụ 6 thành viên: `docs/TEAM_TASKS_6_MEMBERS.md`

## 7) Roadmap ngắn hạn
1. Hoàn thiện annotate polygon slot.
2. Hoàn thiện detector baseline.
3. Thêm layer persistence ổn định (DB/API).
4. Hoàn thiện dashboard và kịch bản demo.
