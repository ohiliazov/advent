from advent.common import load_data


def parse_line(line: str) -> list[int]:
    return list(map(int, line.split()))


def solve_part1(data: list[str]) -> int:
    data = list(map(parse_line, data))
    s = 0
    for history in data:
        while any(history):
            s += history[-1]
            history = [
                history[i] - history[i - 1] for i in range(1, len(history))
            ]
    return s


def solve_part2(data: list[str]) -> int:
    data = list(map(parse_line, data))
    s = 0
    for history in data:
        value_stack = []
        while any(history):
            value_stack.append(history[0])
            history = [
                history[i] - history[i - 1] for i in range(1, len(history))
            ]
        value = 0
        while value_stack:
            item = value_stack.pop()
            value = item - value
        s += value
    return s


if __name__ == "__main__":
    input_data = load_data("day09.txt")
    print(f"Day 9. Part 1: {solve_part1(input_data)}")
    print(f"Day 9. Part 2: {solve_part2(input_data)}")
