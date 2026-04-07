"""Domain contracts (skeleton).

TODO:
- Chuẩn hóa kiểu dữ liệu frame.
- Bổ sung interface event publisher (WebSocket/API).
"""

from abc import ABC, abstractmethod


class SlotRepository(ABC):
    @abstractmethod
    def get_slots(self):
        """TODO: Trả về danh sách slot."""
        raise NotImplementedError

    @abstractmethod
    def save_slots(self, slots):
        """TODO: Lưu trạng thái slot."""
        raise NotImplementedError


class SlotDetector(ABC):
    @abstractmethod
    def detect(self, frame, slots):
        """TODO: Trả về observations theo từng slot."""
        raise NotImplementedError
