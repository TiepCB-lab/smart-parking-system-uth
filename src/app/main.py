"""Application entrypoint."""

import sys
from pathlib import Path
import numpy as np

# Thêm project root vào sys.path để python nhận diện các module src.*
project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

from src.application.use_cases.process_video import ProcessVideoUseCase
from src.cv_pipeline.background_subtraction import BackgroundSubtractionDetector
from src.cv_pipeline.perspective_transform import calculate_perspective_matrix
from src.infrastructure.repositories.json_slot_repository import JsonSlotRepository
from src.presentation.video_controller import VideoController
from src.presentation.point_selector import select_4_points

def build_controller() -> VideoController:
    repository = JsonSlotRepository(project_root / "config" / "slots.json")
    detector = BackgroundSubtractionDetector()
    use_case = ProcessVideoUseCase(detector=detector, repository=repository)
    return VideoController(use_case, show_window=True)

def main() -> None:
    # Nguồn video: đổi thành đường dẫn file video thật của bạn (VD: "data/videos/parking_lot_1.mp4")
    # Nếu dùng webcam thật, để số 0
    VIDEO_SOURCE = 0 
    
    WARP_WIDTH = 800
    WARP_HEIGHT = 600

    print("--- KHỞI TẠO HỆ THỐNG SMART PARKING ---")
    # 1. Lấy tọa độ 4 góc bãi xe để làm Bird-eye view
    points = select_4_points(VIDEO_SOURCE)
    
    matrix = None
    if len(points) == 4:
        print(f"Đã lấy 4 điểm: {points}. Đang tính toán ma trận phối cảnh...")
        matrix = calculate_perspective_matrix(points, WARP_WIDTH, WARP_HEIGHT)
    else:
        print("Cảnh báo: Không chọn đủ 4 điểm. Sẽ chạy pipeline gốc không có Bird-eye view.")

    # 2. Chạy Controller
    controller = build_controller()
    print("Đang chạy luồng giám sát. Nhấn 'q' tại cửa sổ video để thoát.")
    
    # Truyền ma trận vào controller để xử lý
    controller.run(source=VIDEO_SOURCE, perspective_matrix=matrix, warp_dim=(WARP_WIDTH, WARP_HEIGHT))

if __name__ == "__main__":
    main()