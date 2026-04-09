"""Morphology helpers for cleaning binary masks."""

from __future__ import annotations

import cv2
import numpy as np


def clean_mask(mask: np.ndarray, kernel_size: int = 3, iterations: int = 2) -> np.ndarray:
    kernel = np.ones((kernel_size, kernel_size), dtype=np.uint8)
    opened = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=iterations)
    return cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel, iterations=iterations)