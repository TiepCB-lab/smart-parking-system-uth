"""Slot region extraction helpers."""

from __future__ import annotations

from collections.abc import Sequence

import numpy as np

from src.domain.entities import Slot


def extract_slot_regions(frame: np.ndarray, slots: Sequence[Slot]):
    slot_regions: list[tuple[Slot, np.ndarray]] = []
    for slot in slots:
        if not slot.polygon:
            slot_regions.append((slot, frame[0:0, 0:0]))
            continue

        xs = [point[0] for point in slot.polygon]
        ys = [point[1] for point in slot.polygon]
        min_x = max(min(xs), 0)
        min_y = max(min(ys), 0)
        max_x = max(max(xs), min_x)
        max_y = max(max(ys), min_y)
        slot_regions.append((slot, frame[min_y:max_y, min_x:max_x]))

    return slot_regions