"""Background subtraction stage for occupancy detection."""

from __future__ import annotations

from collections.abc import Sequence

import cv2
import numpy as np

from src.cv_pipeline.classifier import classify_slot_region
from src.cv_pipeline.contour_detection import detect_contours
from src.cv_pipeline.morphology import clean_mask
from src.cv_pipeline.preprocessing import preprocess_frame
from src.cv_pipeline.slot_extraction import extract_slot_regions
from src.cv_pipeline.thresholding import apply_threshold
from src.domain.entities import FrameResult, Slot
from src.domain.interfaces import SlotDetector


class BackgroundSubtractionDetector(SlotDetector):
    def __init__(self, history: int = 500, var_threshold: float = 16.0) -> None:
        self.background_subtractor = cv2.createBackgroundSubtractorMOG2(
            history=history,
            varThreshold=var_threshold,
            detectShadows=False,
        )

    def detect(self, frame: np.ndarray, slots: Sequence[Slot], perspective_matrix: np.ndarray | None = None) -> FrameResult:
        preprocessed_frame = preprocess_frame(frame, perspective_matrix=perspective_matrix)
        foreground_mask = self.background_subtractor.apply(preprocessed_frame)
        binary_mask = apply_threshold(foreground_mask)
        cleaned_mask = clean_mask(binary_mask)

        contours = detect_contours(cleaned_mask)
        slot_regions = extract_slot_regions(cleaned_mask, slots)

        updated_slots: list[Slot] = []
        for slot, region in slot_regions:
            status, confidence = classify_slot_region(region, contours=contours)
            updated_slots.append(
                Slot(
                    slot_id=slot.slot_id,
                    polygon=slot.polygon,
                    status=status,
                    confidence=confidence,
                )
            )

        return FrameResult(slots=updated_slots)