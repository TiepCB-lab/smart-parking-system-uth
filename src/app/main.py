"""Application entrypoint."""

from pathlib import Path

from src.application.use_cases.process_video import ProcessVideoUseCase
from src.cv_pipeline.background_subtraction import BackgroundSubtractionDetector
from src.infrastructure.repositories.json_slot_repository import JsonSlotRepository
from src.presentation.video_controller import VideoController


def build_controller() -> VideoController:
    project_root = Path(__file__).resolve().parents[2]
    repository = JsonSlotRepository(project_root / "config" / "slots.json")
    detector = BackgroundSubtractionDetector()
    use_case = ProcessVideoUseCase(detector=detector, repository=repository)
    return VideoController(use_case)


def main() -> None:
    controller = build_controller()
    controller.run(source=0)


if __name__ == "__main__":
    main()
