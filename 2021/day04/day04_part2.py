from typing import List, Tuple
import pytest
from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=4)  # TODO: adjust day!
puzzle_input = puzzle.input_data


def parse(puzzle_input: str) -> Tuple:
    """parse input"""
    drawn_numbers = [int(draw) for draw in puzzle_input.splitlines()[0].split(",")]
    cards = [
        [int(number) for number in card_line.split(" ") if number.strip()]
        for card_line in puzzle_input.splitlines()[2:]
        if card_line.strip()
    ]
    cards = [cards[idx : idx + 5] for idx in range(0, len(cards), 5)]  # type: ignore
    return drawn_numbers, cards


def check_row(row: List):
    return all(item == "X" for item in row)


def check_rows(card):
    for row in card:
        if check_row(row):
            return True


def check_column(card):
    transposed_card = list(zip(*card))
    for row in transposed_card:
        if check_row(row):
            return True


def is_winner(card):
    if check_rows(card) or check_column(card):
        return True


def solve(data: Tuple) -> int:
    """solve puzzle"""
    cards = data[1]
    last_winner = -1
    seen = set()
    for number in data[0]:
        for card_index, card in enumerate(cards):
            for row in card:
                for idx, item in enumerate(row):
                    if item == number:
                        row[idx] = "X"
            if is_winner(card) and card_index not in seen:
                card_sum = sum(
                    sum(filter(lambda i: isinstance(i, int), row)) for row in card
                )
                last_winner = card_sum * number
                seen.add(card_index)

    return last_winner


INPUT_EXAMPLE = """\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""
OUTPUT_EXAMPLE = 1924


@pytest.mark.parametrize(
    ("input_example", "expected"),
    ((INPUT_EXAMPLE, OUTPUT_EXAMPLE),),
)
def test_solve(input_example: str, expected: int) -> None:
    assert solve(parse(input_example)) == expected


def main(puzzle_input: str) -> int:
    """Solve the puzzle for the given input"""
    solution = solve(parse(puzzle_input))
    print(f"Solution: {solution}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(puzzle_input))
