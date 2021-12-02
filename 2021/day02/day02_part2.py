from typing import List
import pytest
from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=2)  # TODO: adjust day!
puzzle_input = puzzle.input_data


def parse(puzzle_input: str) -> List:
    """parse input"""
    data = [line for line in puzzle_input.splitlines()]
    return data


def solve(data: List) -> int:
    """solve puzzle"""

    horizontal = 0
    depth = 0
    aim = 0
    for maneuver in data:
        direction = maneuver.split(" ")[0]
        number = int(maneuver.split(" ")[1])
        if direction == "forward":
            horizontal += number
            depth += number * aim
        elif direction == "up":
            aim -= number
        elif direction == "down":
            aim += number
    final_position = horizontal * depth
    return final_position


INPUT_EXAMPLE = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""
OUTPUT_EXAMPLE = 900


@pytest.mark.parametrize(
    ("input_example", "expected"),
    ((INPUT_EXAMPLE, OUTPUT_EXAMPLE),),
)
def test_solve(input_example: str, expected: int) -> None:
    assert solve(parse(input_example)) == expected


def main(puzzle_input):
    """Solve the puzzle for the given input"""
    solution = solve(parse(puzzle_input))
    print(f"Solution Part 1: {solution}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(puzzle_input))
