"""Domain contracts for repositories and detectors."""

from abc import ABC, abstractmethod
from collections.abc import Sequence

from src.domain.entities import FrameResult, Slot


class SlotRepository(ABC):
    @abstractmethod
    def get_slots(self) -> list[Slot]:
        raise NotImplementedError

    @abstractmethod
    def save_slots(self, slots: Sequence[Slot]) -> None:
        raise NotImplementedError


class SlotDetector(ABC):
    @abstractmethod
    def detect(self, frame, slots: Sequence[Slot]) -> FrameResult:
        raise NotImplementedError
