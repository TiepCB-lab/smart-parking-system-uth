"""Domain entities (skeleton).

TODO:
- Bổ sung validation cho polygon.
- Thêm metadata (camera_id, zone_id, ...).
"""

from dataclasses import dataclass


@dataclass
class ParkingSlot:
    slot_id: str
    polygon: list[tuple[int, int]]
    status: str = "unknown"


@dataclass
class SlotObservation:
    slot_id: str
    status: str
    confidence: float
