from dataclasses import dataclass

from advent.common import load_data

BEAM_DIRECTIONS = {
    "|": {
        "left": {"up", "down"},
        "right": {"up", "down"},
        "up": {"up"},
        "down": {"down"},
    },
    "-": {
        "left": {"left"},
        "right": {"right"},
        "up": {"left", "right"},
        "down": {"left", "right"},
    },
    "\\": {
        "left": {"up"},
        "right": {"down"},
        "up": {"left"},
        "down": {"right"},
    },
    "/": {
        "left": {"down"},
        "right": {"up"},
        "up": {"right"},
        "down": {"left"},
    },
}


@dataclass(frozen=True)
class Beam:
    row: int
    column: int
    direction: str


class Solution:
    def __init__(self, data: list[str]):
        self.grid = data
        self.size = len(self.grid)

    def _turn_once(self, beam: Beam) -> set[Beam]:
        direction = self.grid[beam.row][beam.column]
        if direction == ".":
            return {beam}

        return {
            Beam(row=beam.row, column=beam.column, direction=new_direction)
            for new_direction in BEAM_DIRECTIONS[
                self.grid[beam.row][beam.column]
            ][beam.direction]
        }

    def _move_once(self, beam: Beam) -> Beam | None:
        row = beam.row
        column = beam.column
        direction = beam.direction

        match beam.direction:
            case "up" if beam.row > 0:
                row -= 1
            case "down" if beam.row < self.size - 1:
                row += 1
            case "left" if beam.column > 0:
                column -= 1
            case "right" if beam.column < self.size - 1:
                column += 1
        if row == beam.row and column == beam.column:
            return None
        return Beam(row=row, column=column, direction=direction)

    def _move_beam(self, beam: Beam) -> set[Beam]:
        new_beams = set()
        for turned_beam in self._turn_once(beam):
            if moved_beam := self._move_once(turned_beam):
                new_beams.add(moved_beam)
        return new_beams

    def solve(self, initial_beam: Beam) -> int:
        explored: set[Beam] = set()

        beams = {initial_beam}

        while beams:
            beam = beams.pop()

            if beam in explored:
                continue

            beams |= self._move_beam(beam)
            explored.add(beam)

        return len(
            {(energized.row, energized.column) for energized in explored}
        )

    def solve_part1(self):
        return self.solve(Beam(row=0, column=0, direction="right"))

    def solve_part2(self):
        initial_beams = set()
        for i in range(self.size):
            initial_beams |= {
                Beam(row=i, column=0, direction="right"),
                Beam(row=i, column=self.size - 1, direction="left"),
                Beam(row=self.size - 1, column=i, direction="up"),
                Beam(row=0, column=i, direction="down"),
            }
        res = 0
        for initial_beam in initial_beams:
            res = max(self.solve(initial_beam), res)
        return res


if __name__ == "__main__":
    input_data = load_data("day16.txt")
    board = Solution(input_data)
    print(f"Day 16. Part 1: {board.solve_part1()}")
    print(f"Day 16. Part 2: {board.solve_part2()}")
