"""Preprocessing helpers for video frames."""

from __future__ import annotations

from typing import Literal

import cv2
import numpy as np
from src.cv_pipeline.perspective_transform import apply_bird_eye_view

def to_grayscale(frame: np.ndarray) -> np.ndarray:
    if frame.ndim == 2:
        return frame
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

def resize_frame(frame: np.ndarray, width: int | None = None, height: int | None = None) -> np.ndarray:
    if width is None and height is None:
        return frame

    original_height, original_width = frame.shape[:2]
    if width is None:
        scale = height / float(original_height)
        width = int(original_width * scale)
    elif height is None:
        scale = width / float(original_width)
        height = int(original_height * scale)

    return cv2.resize(frame, (int(width), int(height)), interpolation=cv2.INTER_AREA)


def apply_blur(frame: np.ndarray, kernel_size: int = 5, method: Literal["gaussian", "median"] = "gaussian") -> np.ndarray:
    kernel_size = kernel_size if kernel_size % 2 == 1 else kernel_size + 1
    if method == "median":
        return cv2.medianBlur(frame, kernel_size)
    return cv2.GaussianBlur(frame, (kernel_size, kernel_size), 0)

def preprocess_frame(
    frame: np.ndarray,
    perspective_matrix: np.ndarray | None = None,
    warp_width: int = 800,
    warp_height: int = 600,
    resize_width: int | None = None,
    resize_height: int | None = None,
    blur_kernel_size: int = 5,
    blur_method: Literal["gaussian", "median"] = "gaussian",
) -> np.ndarray:
    """
    Tiền xử lý chuẩn: Kéo phẳng (nếu có ma trận) -> Resize -> Chuyển xám -> Làm mờ.
    """
    processed = frame.copy()
    
    # Kỹ thuật Chương 3: Biến đổi hình học
    if perspective_matrix is not None:
        processed = apply_bird_eye_view(processed, perspective_matrix, warp_width, warp_height)

    processed = resize_frame(processed, width=resize_width, height=resize_height)
        
    # Kỹ thuật Chương 2: Xử lý ảnh cơ bản
    processed = to_grayscale(processed)
    processed = apply_blur(processed, kernel_size=blur_kernel_size, method=blur_method)
    
    return processed