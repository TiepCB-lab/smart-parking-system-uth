"""Optional lightweight classifier for slot regions."""

from __future__ import annotations

from collections.abc import Sequence

import cv2
import numpy as np


def classify_slot_region(region: np.ndarray, contours: Sequence | None = None, occupied_threshold: float = 0.08) -> tuple[str, float]:
    if region.size == 0:
        return "unknown", 0.0

    non_zero_ratio = float(cv2.countNonZero(region)) / float(region.size)
    if non_zero_ratio >= occupied_threshold:
        return "occupied", min(1.0, non_zero_ratio)

    return "free", max(0.0, 1.0 - non_zero_ratio)