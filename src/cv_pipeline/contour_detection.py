"""Contour detection helpers."""

from __future__ import annotations

import cv2
import numpy as np


def detect_contours(mask: np.ndarray, min_area: float = 100.0):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return [contour for contour in contours if cv2.contourArea(contour) >= min_area]