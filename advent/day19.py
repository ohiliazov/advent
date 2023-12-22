from advent.common import load_data


def split_range(
    r: tuple[int, int], op: str, value: int
) -> tuple[tuple[int, int], tuple[int, int]]:
    x, y = r
    if x < value < y:
        if op == "<":
            return (x, value), (value, y)
        elif op == ">":
            return (value + 1, y), (x, value + 1)

    return (0, 0), (x, y)


def calculate(xmas: dict[str, tuple[int, int]]) -> int:
    s = 1
    for min_value, max_value in xmas.values():
        s *= max_value - min_value
    return s


class Solution:
    def __init__(self, data: list[str]):
        self.lines = data

    def process_instructions(self, line: str) -> tuple[str, list[str]]:
        name, instructions = line[:-1].split("{")
        return name, instructions.split(",")

    def process_values(self, line: str) -> list[int]:
        data = []
        for item in line[1:-1].split(","):
            key, value = item.split("=")
            data.append(int(value))
        return data

    def solve_part1(self):
        split_idx = self.lines.index("")
        instructions = dict(
            map(self.process_instructions, self.lines[:split_idx])
        )

        res = 0
        for x, m, a, s in map(
            self.process_values, self.lines[split_idx + 1 :]
        ):
            start = "in"

            while True:
                value = None
                for item in instructions[start]:
                    if ":" not in item:
                        met, value = True, item
                    else:
                        condition, value = item.split(":")
                        met = eval(condition)

                    if met:
                        break

                if value in ["A", "R"]:
                    if value == "A":
                        res += x + m + a + s
                    break
                else:
                    start = value

        return res

    def calculate(self, xmas: dict[str, tuple[int, int]]) -> int:
        s = 1
        for min_value, max_value in xmas.values():
            s *= max_value - min_value
        return s

    def solve_part2(self):
        split_idx = self.lines.index("")
        instructions = dict(
            map(self.process_instructions, self.lines[:split_idx])
        )

        to_check = [
            (
                "in",
                {
                    "x": (1, 4001),
                    "m": (1, 4001),
                    "a": (1, 4001),
                    "s": (1, 4001),
                },
            )
        ]
        res = 0
        while to_check:
            name, xmas = to_check.pop()

            for item in instructions[name]:
                sub_xmas = xmas.copy()
                if ":" in item:
                    condition, item = item.split(":")
                    letter = condition[0]
                    op = condition[1]
                    value = int(condition[2:])
                    met, unmet = split_range(xmas[letter], op, value)
                    sub_xmas[letter] = met
                    xmas[letter] = unmet
                    if item == "A":
                        res += calculate(sub_xmas)
                    elif item != "R":
                        to_check.append((item, sub_xmas.copy()))
                elif item == "A":
                    res += calculate(xmas)
                elif item != "R":
                    to_check.append((item, xmas.copy()))
                else:
                    break

        return res


if __name__ == "__main__":
    input_data = load_data("day19.txt")
    board = Solution(input_data)
    print(f"Day 19. Part 1: {board.solve_part1()}")
    print(f"Day 19. Part 2: {board.solve_part2()}")
