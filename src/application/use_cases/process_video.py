"""Application use-case for a single video frame."""

from src.domain.entities import FrameResult


class ProcessVideoUseCase:
    def __init__(self, detector, repository) -> None:
        self.detector = detector
        self.repository = repository

    def run_frame(self, frame) -> FrameResult:
        slots = self.repository.get_slots()
        frame_result = self.detector.detect(frame, slots)
        self.repository.save_slots(frame_result.slots)
        return frame_result
