from typing import List
import pytest
from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=3)  # TODO: adjust day!
puzzle_input = puzzle.input_data


def parse(puzzle_input: str) -> List:
    """parse input"""
    data = [int(line) for line in puzzle_input.splitlines()]
    return data


def solve(data: List) -> int:
    """solve puzzle"""
    # return solution


INPUT_EXAMPLE = """\
"""
OUTPUT_EXAMPLE = 5


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
