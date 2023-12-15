from advent.utils import load_data


def transpose(data: list[str]) -> list[str]:
    transposed = []
    for i in range(len(data[0])):
        new_row = ""
        for j in range(len(data)):
            new_row += data[j][i]
        transposed.append(new_row)
    return transposed


def cycle(data: tuple[str]) -> tuple[str]:
    for _ in range(4):
        data = rot90(tuple(map(roll_row, data)))

    return tuple(data)


def rot90(data: tuple[str]) -> list[str]:
    rotated = []
    for i in range(len(data[0]) - 1, -1, -1):
        new_row = ""
        for j in range(len(data[0])):
            new_row += data[j][i]
        rotated.append(new_row)

    return rotated


def roll_row(row: str) -> str:
    new_row = ""
    dot_count = 0
    for rock in row:
        if rock == ".":
            dot_count += 1
        elif rock == "O":
            new_row += "O"
        else:
            new_row += "." * dot_count + "#"
            dot_count = 0

    return new_row + "." * dot_count


def count_load(data: list[str]) -> int:
    s = 0
    for line in data:
        for rock_idx, rock in enumerate(line):
            if rock == "O":
                s += len(line) - rock_idx
    return s


class Solution:
    def __init__(self, data: list[str]):
        self.data = transpose(data)

    def solve_part1(self):
        return count_load(list(map(roll_row, self.data)))

    def solve_part2(self):
        data = tuple(self.data)

        loops = {}

        for idx in range(1_000_000_000):
            new_data = cycle(data)
            if new_data not in loops:
                loops[new_data] = idx
            elif (1_000_000_000 - idx) % (loops[new_data] - idx) == 0:
                break

            data = new_data

        return count_load(data)


if __name__ == "__main__":
    input_data = load_data("day14.txt")
    board = Solution(input_data)
    print(f"Day 14. Part 1: {board.solve_part1()}")
    print(f"Day 14. Part 2: {board.solve_part2()}")
