"""Presentation controller (skeleton).

TODO:
- Thêm CLI args cho camera/video file.
- Vẽ overlay (polygon + trạng thái) trên frame.
"""


class VideoController:
    def __init__(self, use_case) -> None:
        self.use_case = use_case

    def run(self, source=0):
        """TODO: Mở stream, đọc frame, gọi use_case, hiển thị."""
        _ = source
        return None
