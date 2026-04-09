"""Preprocessing helpers for video frames."""

from __future__ import annotations

import cv2
import numpy as np


def to_grayscale(frame: np.ndarray) -> np.ndarray:
    if frame.ndim == 2:
        return frame
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


def apply_blur(frame: np.ndarray, kernel_size: int = 5) -> np.ndarray:
    kernel_size = kernel_size if kernel_size % 2 == 1 else kernel_size + 1
    return cv2.GaussianBlur(frame, (kernel_size, kernel_size), 0)


def preprocess_frame(frame: np.ndarray) -> np.ndarray:
    return apply_blur(to_grayscale(frame))