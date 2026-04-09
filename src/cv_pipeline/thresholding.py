"""Thresholding helpers for foreground masks."""

from __future__ import annotations

import cv2
import numpy as np


def apply_threshold(mask: np.ndarray, threshold_value: int = 127, max_value: int = 255) -> np.ndarray:
    _, binary_mask = cv2.threshold(mask, threshold_value, max_value, cv2.THRESH_BINARY)
    return binary_mask