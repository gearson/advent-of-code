from typing import List
from collections import Counter
import pytest
from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=6)  # TODO: adjust day!
puzzle_input = puzzle.input_data


def parse(puzzle_input: str) -> List:
    """parse input"""
    data = [int(fish) for fish in puzzle_input.split(",")]
    return data


def solve(data: List) -> int:
    """solve puzzle"""
    days = 0
    fish_counter = Counter(fish for fish in data)
    while days != 256:
        fish_counter_helper = Counter({8: fish_counter[0], 6: fish_counter[0]})
        for fish_status, number in fish_counter.items():
            if fish_status >= 1:
                fish_counter_helper[fish_status - 1] += number
        fish_counter = fish_counter_helper
        days += 1
    return sum(fish_counter.values())


INPUT_EXAMPLE = """\
3,4,3,1,2
"""
OUTPUT_EXAMPLE = 26984457539


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
