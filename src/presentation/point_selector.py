"""Utility to select 4 points from a video frame for perspective transform."""

import cv2
import numpy as np

def select_4_points(video_source: str | int) -> list[tuple[int, int]]:
    cap = cv2.VideoCapture(video_source)
    success, frame = cap.read()
    cap.release()

    if not success:
        print(f"Lỗi: Không thể đọc video từ nguồn {video_source}")
        return []

    points = []
    window_name = "Click 4 diem (Trai-Tren, Phai-Tren, Phai-Duoi, Trai-Duoi)"

    def mouse_callback(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN and len(points) < 4:
            points.append((x, y))
            cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)
            cv2.imshow(window_name, frame)

    cv2.imshow(window_name, frame)
    cv2.setMouseCallback(window_name, mouse_callback)

    print("Hãy click 4 điểm trên cửa sổ video theo thứ tự: Trái-Trên, Phải-Trên, Phải-Dưới, Trái-Dưới.")
    print("Nhấn phím bất kỳ sau khi chọn xong.")
    
    while len(points) < 4:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    return points