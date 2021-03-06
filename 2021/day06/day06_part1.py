from typing import List
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
    while days != 80:
        new_borns = 0
        for idx, fish in enumerate(data):
            if fish == 0:
                data[idx] = 6
                new_borns += 1
            else:
                data[idx] = fish - 1
        days += 1
        data.extend([8] * new_borns)
        print(days)

    return len(data)


INPUT_EXAMPLE = """\
3,4,3,1,2
"""
OUTPUT_EXAMPLE = 5934


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
