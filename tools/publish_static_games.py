from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "labs" / "docs" / "games"
TARGET = ROOT / "_site" / "games"


def main() -> None:
    if not SOURCE.exists():
        return

    TARGET.mkdir(parents=True, exist_ok=True)

    for game_dir in SOURCE.iterdir():
        if not game_dir.is_dir():
            continue

        destination = TARGET / game_dir.name
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(game_dir, destination)


if __name__ == "__main__":
    main()
