from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"


def load_data(name: str) -> list[str]:
    data_path = DATA_DIR / name

    with data_path.open() as f:
        return [line.strip() for line in f.readlines()]
