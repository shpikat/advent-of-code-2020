from typing import List, Tuple


def read_requirements(filename: str) -> List[Tuple[int, int]]:
    with open(filename, "r") as file:
        file.readline()
        return [(int(number), i)
                for i, number in enumerate(file.readline().split(','))
                if number != 'x']


def solve(filename: str) -> int:
    requirements = read_requirements(filename)

    timestamp = 0
    step = 1
    for interval, gap in requirements:
        while timestamp < interval:
            timestamp += step
        while (timestamp + gap) % interval != 0:
            timestamp += step
        step *= interval
    return timestamp
