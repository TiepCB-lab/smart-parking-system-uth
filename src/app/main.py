"""Application entrypoint (skeleton).

TODO:
- Tạo dependency injection rõ ràng theo config/env.
- Kết nối logger + config loader.
"""

from pathlib import Path

from src.application.use_cases.process_video import ProcessVideoUseCase
from src.infrastructure.opencv.background_detector import BackgroundSubtractionDetector
from src.infrastructure.repositories.json_slot_repository import JsonSlotRepository
from src.presentation.video_controller import VideoController


def build_controller() -> VideoController:
    repository = JsonSlotRepository(Path("config/slots.json"))
    detector = BackgroundSubtractionDetector()
    use_case = ProcessVideoUseCase(detector=detector, repository=repository)
    return VideoController(use_case)


def main() -> None:
    """TODO: parse args rồi truyền source phù hợp."""
    controller = build_controller()
    controller.run(source=0)


if __name__ == "__main__":
    main()
