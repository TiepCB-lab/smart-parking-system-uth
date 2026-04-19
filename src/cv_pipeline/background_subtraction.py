"""Background subtraction stage for occupancy detection."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Literal

import cv2
import numpy as np

from src.cv_pipeline.morphology import clean_mask
from src.cv_pipeline.preprocessing import preprocess_frame
from src.cv_pipeline.slot_extraction import extract_slot_regions
from src.cv_pipeline.thresholding import apply_threshold
from src.domain.entities import FrameResult, Slot
from src.domain.interfaces import SlotDetector


class BackgroundSubtractionDetector(SlotDetector):
    def __init__(
        self,
        subtractor_type: Literal["mog2", "knn"] = "mog2",
        history: int = 500,
        var_threshold: float = 16.0,
        dist2_threshold: float = 400.0,
        detect_shadows: bool = False,
        default_foreground_threshold: float = 0.08,
        slot_foreground_thresholds: dict[str, float] | None = None,
    ) -> None:
        self.subtractor_type = subtractor_type.lower()
        self.default_foreground_threshold = default_foreground_threshold
        self.slot_foreground_thresholds = slot_foreground_thresholds or {}
        self.background_subtractor = self._create_background_subtractor(
            subtractor_type=self.subtractor_type,
            history=history,
            var_threshold=var_threshold,
            dist2_threshold=dist2_threshold,
            detect_shadows=detect_shadows,
        )

    def _create_background_subtractor(
        self,
        subtractor_type: Literal["mog2", "knn"],
        history: int,
        var_threshold: float,
        dist2_threshold: float,
        detect_shadows: bool,
    ):
        if subtractor_type == "knn":
            return cv2.createBackgroundSubtractorKNN(
                history=history,
                dist2Threshold=dist2_threshold,
                detectShadows=detect_shadows,
            )

        if subtractor_type != "mog2":
            raise ValueError(
                f"Unsupported subtractor_type '{subtractor_type}'. Use 'mog2' or 'knn'."
            )

        return cv2.createBackgroundSubtractorMOG2(
            history=history,
            varThreshold=var_threshold,
            detectShadows=detect_shadows,
        )

    @staticmethod
    def _foreground_ratio(region: np.ndarray) -> float:
        if region.size == 0:
            return 0.0
        return float(cv2.countNonZero(region)) / float(region.size)

    def _slot_threshold(self, slot_id: str) -> float:
        threshold = self.slot_foreground_thresholds.get(slot_id, self.default_foreground_threshold)
        return max(0.0, min(1.0, float(threshold)))

    def detect(self, frame: np.ndarray, slots: Sequence[Slot], perspective_matrix: np.ndarray | None = None) -> FrameResult:
        preprocessed_frame = preprocess_frame(frame, perspective_matrix=perspective_matrix)
        foreground_mask = self.background_subtractor.apply(preprocessed_frame)
        binary_mask = apply_threshold(foreground_mask)
        cleaned_mask = clean_mask(binary_mask)

        slot_regions = extract_slot_regions(cleaned_mask, slots)

        updated_slots: list[Slot] = []
        for slot, region in slot_regions:
            ratio = self._foreground_ratio(region)
            threshold = self._slot_threshold(slot.slot_id)
            if region.size == 0:
                status, confidence = "unknown", 0.0
            elif ratio >= threshold:
                status, confidence = "occupied", min(1.0, ratio)
            else:
                status, confidence = "free", max(0.0, 1.0 - ratio)

            updated_slots.append(
                Slot(
                    slot_id=slot.slot_id,
                    polygon=slot.polygon,
                    status=status,
                    confidence=confidence,
                )
            )

        return FrameResult(slots=updated_slots)