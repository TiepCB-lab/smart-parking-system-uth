"""JSON repository adapter for parking slots."""

from __future__ import annotations

import json
from collections.abc import Sequence
from pathlib import Path

from src.domain.entities import Slot
from src.domain.interfaces import SlotRepository


class JsonSlotRepository(SlotRepository):
    def __init__(self, data_file: Path) -> None:
        self.data_file = data_file

    def _resolve_source_file(self) -> Path:
        if self.data_file.exists():
            return self.data_file

        example_file = self.data_file.with_name(f"{self.data_file.stem}.example{self.data_file.suffix}")
        if example_file.exists():
            return example_file

        return self.data_file

    def get_slots(self) -> list[Slot]:
        source_file = self._resolve_source_file()
        if not source_file.exists():
            return []

        with source_file.open("r", encoding="utf-8") as file_handle:
            raw_slots = json.load(file_handle)

        slots: list[Slot] = []
        for item in raw_slots:
            polygon = [tuple(point) for point in item.get("polygon", [])]
            slots.append(
                Slot(
                    slot_id=str(item.get("slot_id", "")),
                    polygon=polygon,
                    status=str(item.get("status", "unknown")),
                    confidence=float(item.get("confidence", 0.0)),
                )
            )

        return slots

    def save_slots(self, slots: Sequence[Slot]) -> None:
        self.data_file.parent.mkdir(parents=True, exist_ok=True)

        payload = [
            {
                "slot_id": slot.slot_id,
                "polygon": [list(point) for point in slot.polygon],
                "status": slot.status,
                "confidence": slot.confidence,
            }
            for slot in slots
        ]

        with self.data_file.open("w", encoding="utf-8") as file_handle:
            json.dump(payload, file_handle, indent=2, ensure_ascii=True)
