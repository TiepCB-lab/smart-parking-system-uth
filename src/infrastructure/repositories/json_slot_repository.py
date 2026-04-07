"""JSON repository adapter (skeleton).

TODO:
- Validate schema JSON.
- Hỗ trợ versioning file cấu hình.
"""

from pathlib import Path


class JsonSlotRepository:
    def __init__(self, data_file: Path) -> None:
        self.data_file = data_file

    def get_slots(self):
        """TODO: Đọc file JSON và parse về ParkingSlot."""
        return []

    def save_slots(self, slots):
        """TODO: Ghi ngược trạng thái slot vào JSON/DB."""
        _ = slots
