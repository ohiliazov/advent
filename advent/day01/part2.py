from advent.utils import load_data

digits = {
    "1": "1",
    "one": "1",
    "2": "2",
    "two": "2",
    "3": "3",
    "three": "3",
    "4": "4",
    "four": "4",
    "5": "5",
    "five": "5",
    "6": "6",
    "six": "6",
    "7": "7",
    "seven": "7",
    "8": "8",
    "eight": "8",
    "9": "9",
    "nine": "9",
}


def solve_line(line: str):
    i, j = (
        0,
        -1,
    )
    x = None
    y = None
    while x is None:
        for key, value in digits.items():
            if line[i:].startswith(key):
                x = value
                break
        i += 1

    while y is None:
        for key, value in digits.items():
            if line[j:].startswith(key):
                y = value
                break
        j -= 1

    return int(str(x) + str(y))


def solve(data: list[str]) -> int:
    return sum(solve_line(line) for line in data)


if __name__ == "__main__":
    input_data = load_data("day01.txt")
    print(solve(input_data))
