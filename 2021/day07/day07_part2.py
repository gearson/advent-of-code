from typing import List
import pytest
from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=7)  # TODO: adjust day!
puzzle_input = puzzle.input_data


def parse(puzzle_input: str) -> List:
    """parse input"""
    data = [int(line) for line in puzzle_input.split(",")]
    return data


def solve(data: List) -> int:
    """solve puzzle"""
    max_distance = max(data)
    all_costs = []
    for alignment_position in range(0, max_distance):
        cost_position = []
        for crab_position in data:
            fuel_cost = (
                abs(crab_position - alignment_position)
                * (abs(crab_position - alignment_position) + 1)
                // 2
            )
            cost_position.extend([fuel_cost])
        all_costs.extend([sum(cost_position)])
    return min(all_costs)


INPUT_EXAMPLE = """\
16,1,2,0,4,2,7,1,2,14
"""
OUTPUT_EXAMPLE = 168


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
