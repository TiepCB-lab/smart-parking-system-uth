"""OpenCV video reader adapter."""

from __future__ import annotations

import cv2


class OpenCVVideoReader:
    def __init__(self, source=0) -> None:
        self.source = source
        self.capture = cv2.VideoCapture(source)

    def is_opened(self) -> bool:
        return self.capture.isOpened()

    def read(self):
        return self.capture.read()

    def release(self) -> None:
        self.capture.release()