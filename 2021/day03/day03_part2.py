from collections import Counter
from typing import List
import pytest
from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=3)  # TODO: adjust day!
puzzle_input = puzzle.input_data


def parse(puzzle_input: str) -> List:
    """parse input"""
    data = [line for line in puzzle_input.splitlines()]
    return data


def solve(data: List) -> int:
    """solve puzzle"""
    oxy_list = data
    for idx in range(len(data[0])):
        pos = [line[idx] for line in oxy_list]
        if Counter(pos)["1"] >= Counter(pos)["0"]:
            oxy_list = [line for line in oxy_list if line[idx] == "1"]
        else:
            oxy_list = [line for line in oxy_list if line[idx] == "0"]
        if len(oxy_list) == 1:
            break

    carbon_list = data
    for idx in range(len(data[0])):
        pos = [line[idx] for line in carbon_list]
        if Counter(pos)["1"] < Counter(pos)["0"]:
            carbon_list = [line for line in carbon_list if line[idx] == "1"]
        else:
            carbon_list = [line for line in carbon_list if line[idx] == "0"]
        if len(carbon_list) == 1:
            break

    oxy_int = int("".join(str(x) for x in oxy_list[0]), 2)
    carbon_int = int("".join(str(x) for x in carbon_list[0]), 2)
    return oxy_int * carbon_int


INPUT_EXAMPLE = """\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""
OUTPUT_EXAMPLE = 230


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
