"""Presentation controller for reading and processing video streams."""

from __future__ import annotations

import cv2

from src.infrastructure.opencv.video_reader import OpenCVVideoReader


class VideoController:
    def __init__(self, use_case, show_window: bool = False) -> None:
        self.use_case = use_case
        self.show_window = show_window

    def run(self, source=0, max_frames: int | None = None):
        reader = OpenCVVideoReader(source)
        if not reader.is_opened():
            raise RuntimeError(f"Cannot open video source: {source}")

        processed_frames = 0
        try:
            while True:
                success, frame = reader.read()
                if not success:
                    break

                frame_result = self.use_case.run_frame(frame)
                processed_frames += 1

                if self.show_window:
                    display_frame = frame.copy()
                    occupied_count = sum(1 for slot in frame_result.slots if slot.status == "occupied")
                    summary_text = f"Occupied: {occupied_count}/{len(frame_result.slots)}"
                    cv2.putText(
                        display_frame,
                        summary_text,
                        (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0,
                        (0, 255, 0),
                        2,
                        cv2.LINE_AA,
                    )
                    cv2.imshow("Parking Monitor", display_frame)
                    if cv2.waitKey(1) & 0xFF == ord("q"):
                        break

                if max_frames is not None and processed_frames >= max_frames:
                    break
        finally:
            reader.release()

            if self.show_window:
                cv2.destroyAllWindows()

        return processed_frames
