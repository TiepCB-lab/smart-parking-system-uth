"""Preprocessing helpers for video frames."""

from __future__ import annotations

import cv2
import numpy as np
from src.cv_pipeline.perspective_transform import apply_bird_eye_view

def to_grayscale(frame: np.ndarray) -> np.ndarray:
    if frame.ndim == 2:
        return frame
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

def apply_blur(frame: np.ndarray, kernel_size: int = 5) -> np.ndarray:
    kernel_size = kernel_size if kernel_size % 2 == 1 else kernel_size + 1
    return cv2.GaussianBlur(frame, (kernel_size, kernel_size), 0)

def preprocess_frame(frame: np.ndarray, perspective_matrix: np.ndarray | None = None, warp_width: int = 800, warp_height: int = 600) -> np.ndarray:
    """
    Tiền xử lý: Kéo phẳng (nếu có ma trận) -> Chuyển xám -> Làm mờ.
    """
    processed = frame.copy()
    
    # Kỹ thuật Chương 3: Biến đổi hình học
    if perspective_matrix is not None:
        processed = apply_bird_eye_view(processed, perspective_matrix, warp_width, warp_height)
        
    # Kỹ thuật Chương 2: Xử lý ảnh cơ bản
    processed = to_grayscale(processed)
    processed = apply_blur(processed)
    
    return processed