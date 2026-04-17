"""Presentation controller for reading and processing video streams."""

from __future__ import annotations
import cv2
import numpy as np
from pure_eval import Evaluator
from src.infrastructure.opencv.video_reader import OpenCVVideoReader
from src.cv_pipeline.perspective_transform import apply_bird_eye_view

class VideoController:
    def __init__(self, use_case, show_window: bool = False) -> None:
        self.use_case = use_case
        self.show_window = show_window

    def run(self, source=0, max_frames: int | None = None, perspective_matrix: np.ndarray | None = None, warp_dim=(800, 600)):
        reader = OpenCVVideoReader(source)
        if not reader.is_opened():
            raise RuntimeError(f"Cannot open video source: {source}")

        processed_frames = 0
        try:
            while True:
                success, frame = reader.read()
                if not success:
                    break

                # Chạy pipeline xử lý
                frame_result = self.use_case.detector.detect(frame, self.use_case.repository.get_slots(), perspective_matrix)
                processed_frames += 1

                if Evaluator is not None:
                    Evaluator.evaluate_frame(processed_frames, frame_result.slots)
                
                if self.show_window:
                    # Nếu có matrix, ta phải bóp méo hình gốc để hiển thị cho khớp với hệ tọa độ đã xử lý
                    display_frame = frame.copy()
                    if perspective_matrix is not None:
                        display_frame = apply_bird_eye_view(display_frame, perspective_matrix, warp_dim[0], warp_dim[1])

                    occupied_count = 0
                    # Vẽ các ô đỗ xe lên hình
                    for slot in frame_result.slots:
                        if slot.status == "occupied":
                            color = (0, 0, 255) # Đỏ
                            occupied_count += 1
                        elif slot.status == "free":
                            color = (0, 255, 0) # Xanh lá
                        else:
                            color = (0, 255, 255) # Vàng (unknown)

                        # Vẽ đa giác
                        pts = np.array(slot.polygon, np.int32).reshape((-1, 1, 2))
                        cv2.polylines(display_frame, [pts], True, color, 2)
                        
                        # Ghi tên ô (A1, A2...)
                        text_x, text_y = slot.polygon[0]
                        cv2.putText(display_frame, slot.slot_id, (text_x, text_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

                    # Hiển thị thống kê tổng
                    summary_text = f"Occupied: {occupied_count}/{len(frame_result.slots)}"
                    cv2.putText(display_frame, summary_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 3)
                    cv2.putText(display_frame, summary_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)

                    cv2.imshow("Smart Parking Monitor", display_frame)
                    
                    # Nhấn 'q' để thoát
                    if cv2.waitKey(30) & 0xFF == ord("q"):
                        break

                if max_frames is not None and processed_frames >= max_frames:
                    break
        finally:
            reader.release()
            if self.show_window:
                cv2.destroyAllWindows()
            if Evaluator is not None:
                Evaluator.print_report()
        return processed_frames