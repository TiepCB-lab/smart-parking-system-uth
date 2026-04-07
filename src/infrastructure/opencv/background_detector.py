"""OpenCV detector adapter (skeleton).

TODO:
- Tích hợp thuật toán MOG2/YOLO.
- Viết hàm calibrate threshold theo camera.
"""

import cv2


class BackgroundSubtractionDetector:
    def __init__(self) -> None:
        # TODO: Tinh chỉnh tham số detectShadows/history/varThreshold
        self.background_subtractor = cv2.createBackgroundSubtractorMOG2()

    def detect(self, frame, slots):
        """TODO: Trả về SlotObservation list thật sự."""
        _ = self.background_subtractor.apply(frame)
        return []
