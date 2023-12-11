from advent.utils import load_data
from collections import Counter

PART1_RANKS = "23456789TJQKA"
PART2_RANKS = "J23456789TQKA"


def get_hand_type(hand_counter: dict[str, int]) -> int:
    match max(hand_counter.values()):
        case 5:
            hand_type = 6
        case 4:
            hand_type = 5
        case 3:
            if len(hand_counter) == 2:
                hand_type = 4
            else:
                hand_type = 3
        case 2:
            if len(hand_counter) == 3:
                hand_type = 2
            else:
                hand_type = 1
        case 1:
            hand_type = 0
        case _:
            raise Exception("invalid hand")

    return hand_type


def parse_line_part1(line: str) -> tuple[str, tuple[tuple, int]]:
    hand, bid = line.strip().split()
    hand_counter = Counter(hand)

    hand_rank = (get_hand_type(hand_counter), *map(PART1_RANKS.index, hand))

    return hand, (hand_rank, int(bid))


def parse_line_part2(line: str) -> tuple[str, tuple[tuple, int]]:
    hand, bid = line.strip().split()
    hand_counter = Counter(hand)

    joker_count = hand_counter.pop("J", 0)
    if not hand_counter:
        hand_counter["J"] = 0
    most_common_face = hand_counter.most_common(1)[0][0]
    hand_counter[most_common_face] += joker_count

    hand_rank = (get_hand_type(hand_counter), *map(PART2_RANKS.index, hand))

    return hand, (hand_rank, int(bid))


def solve(data: list[str], parse_func: callable) -> int:
    hands = dict(map(parse_func, data))
    s = 0
    for idx, hand in enumerate(sorted(hands, key=lambda h: hands[h][0]), start=1):
        s += hands[hand][1] * idx
    return s


def solve_part1(data: list[str]) -> int:
    return solve(data, parse_line_part1)


def solve_part2(data: list[str]) -> int:
    return solve(data, parse_line_part2)


if __name__ == "__main__":
    input_data = load_data("day07.txt")
    print(f"Day 7. Part 1: {solve_part1(input_data)}")
    print(f"Day 7. Part 2: {solve_part2(input_data)}")
