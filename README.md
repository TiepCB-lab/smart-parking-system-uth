# smart-parking-system-uth
Phát hiện và giám sát trạng thái chỗ đậu xe từ video bằng Python + OpenCV.

> ⚠️ Hiện tại repository này đang ở mức **khung dự án (skeleton)**: chỉ có cấu trúc + TODO list, chưa triển khai hoàn thiện logic trong bất kỳ module nào.

## 3) Cấu trúc thư mục mới (2026)
```text
backend/
├── extract_frames.py
├── main.py
├── requirements.txt
├── api/
│   ├── routes.py
│   └── websocket_manager.py
├── core_cv/
│   ├── feature_extraction.py
│   ├── pipeline.py
│   ├── preprocessing.py
│   ├── segmentation.py
│   └── train_svm.py
└── frontend/
    └── src/
        ├── App.vue
        ├── components/
        │   ├── BoundingBox.vue
        │   ├── ControlPanel.vue
        │   └── VideoManager.vue
        └── services/
            └── socketClient.js

models/
├── parking_spots_multi.json
└── parking_spots.json

services/
├── camera_manager.py
└── parking_manager.py

tests/
└── evaluate_cv.py

├── data/
frontend/
├── index.html
├── package.json
├── README.md
├── vite.config.js
├── public/
├── src/
│   ├── App.vue
│   ├── main.js
│   ├── style.css
│   ├── assets/
│   └── components/
│       ├── BoundingBox.vue
│       ├── ControlPanel.vue
│       ├── HelloWorld.vue
│       └── VideoManager.vue
│   └── services/
│       └── socketClient.js
```

> **Lưu ý:** Tất cả các file `.py` hiện tại chỉ là stub với nội dung `# TODO`, chưa có logic triển khai.
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
