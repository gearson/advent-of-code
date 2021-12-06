from typing import List
from collections import Counter
import pytest
from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=5)  # TODO: adjust day!
puzzle_input = puzzle.input_data


def parse(puzzle_input: str) -> List:
    """parse input"""
    data = []
    for line in puzzle_input.splitlines():
        start, end = line.split("->")
        x1, y1 = start.split(",")
        x2, y2 = end.split(",")
        x1 = int(x1.strip())
        y1 = int(y1.strip())
        x2 = int(x2.strip())
        y2 = int(y2.strip())
        data.append([x1, y1, x2, y2])

    return data


def solve(data: List) -> int:
    """solve puzzle"""
    points = Counter()
    for line in data:
        x1 = line
        # vertical lines
        if line[0] == line[2]:
            for y in range(min(line[1], line[3]), max(line[1], line[3]) + 1):
                points[(line[0]), y] += 1
        #  horizontal lines
        elif line[1] == line[3]:
            for x in range(min(line[0], line[2]), max(line[0], line[2]) + 1):
                points[x, line[1]] += 1
        # diagonals
        else:
            if line[0] < line[2]:
                x_d = 1
            else:
                x_d = -1
            if line[1] < line[3]:
                y_d = 1
            else:
                y_d = -1
            x, y = line[0], line[1]
            while (x, y) != (line[2] + x_d, line[3] + y_d):
                points[(x, y)] += 1
                x, y = x + x_d, y + y_d

    count = 0
    for coordinate, counter in points.most_common():
        if counter > 1:
            count += 1
    return count
    # return solution


INPUT_EXAMPLE = """\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""
OUTPUT_EXAMPLE = 12


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
