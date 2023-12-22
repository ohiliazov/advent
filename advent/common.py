import dataclasses
from enum import Enum
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"


def load_data(name: str) -> list[str]:
    data_path = DATA_DIR / name

    with data_path.open() as f:
        return [line.strip() for line in f.readlines()]


@dataclasses.dataclass(frozen=True)
class Coord:
    x: int
    y: int

    def __add__(self, other: "Coord") -> "Coord":
        return Coord(self.x + other.x, self.y + other.y)

    def __mul__(self, other: "Coord|int") -> "Coord":
        if isinstance(other, int):
            return Coord(self.x * other, self.y * other)
        return Coord(self.x * other.x, self.y * other.y)

    def __repr__(self) -> str:
        return f"[{self.x} {self.y}]"

    def __lt__(self, other: "Coord") -> bool:
        return self.x < other.x or self.x == other.x and self.y < other.y


class Direction(Enum):
    UP = Coord(-1, 0)
    NORTH = Coord(-1, 0)

    DOWN = Coord(1, 0)
    SOUTH = Coord(1, 0)

    LEFT = Coord(0, -1)
    WEST = Coord(0, -1)

    RIGHT = Coord(0, 1)
    EAST = Coord(0, 1)
