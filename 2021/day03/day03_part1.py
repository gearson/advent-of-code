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
    position_list = []
    most_common_bit = []
    for idx in range(len(data[0])):
        pos = [line[idx] for line in data]
        position_list.append(pos)
    for position in position_list:
        most_common_dict = Counter(position)
        if most_common_dict['0'] > most_common_dict['1']:
            most_common_bit.append(0)
        else:
            most_common_bit.append(1)
    epsilon = [(int(bit)-1)*-1 for bit in most_common_bit]
    epsilon_int = int("".join(str(x) for x in epsilon), 2)
    gamma_int = int("".join(str(x) for x in most_common_bit), 2)
    return gamma_int * epsilon_int


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
OUTPUT_EXAMPLE = 198


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
