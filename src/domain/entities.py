"""Domain entities for parking slot processing."""

from dataclasses import dataclass, field


@dataclass(slots=True)
class Slot:
    slot_id: str
    polygon: list[tuple[int, int]]
    status: str = "unknown"
    confidence: float = 0.0


@dataclass(slots=True)
class FrameResult:
    frame_index: int | None = None
    slots: list[Slot] = field(default_factory=list)
