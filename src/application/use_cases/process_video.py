"""Application use-case (skeleton).

TODO:
- Áp dụng rule smoothing theo nhiều frame.
- Ghi log metric (fps, latency, occupancy rate).
"""


class ProcessVideoUseCase:
    def __init__(self, detector, repository) -> None:
        self.detector = detector
        self.repository = repository

    def run_frame(self, frame):
        """TODO: read slots -> detect -> update -> persist."""
        slots = self.repository.get_slots()
        _ = self.detector.detect(frame, slots)
        self.repository.save_slots(slots)
        return slots
