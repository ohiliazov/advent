from collections import defaultdict

from advent.utils import load_data


def solve(data: list[str]) -> int:
    current_number = ""
    gear_counter = defaultdict(list)

    for row_idx, row in enumerate(data):
        for col_idx in range(len(row) + 1):
            if col_idx < len(row) and row[col_idx].isdigit():
                current_number += row[col_idx]
            elif current_number:
                lc = max(col_idx - len(current_number) - 1, 0)
                rc = min(col_idx + 1, len(row))
                lr = max(row_idx - 1, 0)
                rr = min(row_idx + 2, len(data))

                for r in range(lr, rr):
                    for c in range(lc, rc):
                        if data[r][c] == "*":
                            gear_counter[r, c].append(int(current_number))

                current_number = ""

    return sum(item[0] * item[1] for item in gear_counter.values() if len(item) == 2)


if __name__ == "__main__":
    input_data = load_data("day03.txt")
    print(solve(input_data))
