from typing import List, Tuple


def part1(input_data: str) -> int:
    departure, schedule = read_schedule(input_data)

    min_wait, earliest_bus = min(
        (((departure - 1) // bus + 1) * bus - departure, bus) for bus in schedule
    )
    return min_wait * earliest_bus


def read_schedule(input_data: str) -> Tuple[int, List[int]]:
    lines = input_data.splitlines()
    timestamp = int(lines[0])
    schedule = [int(number) for number in lines[1].split(",") if number != "x"]
    return timestamp, schedule


def part2(input_data: str) -> int:
    requirements = read_requirements(input_data)

    timestamp = 0
    step = 1
    for interval, gap in requirements:
        while timestamp < interval:
            timestamp += step
        while (timestamp + gap) % interval != 0:
            timestamp += step
        step *= interval
    return timestamp


def read_requirements(input_data: str) -> List[Tuple[int, int]]:
    line = input_data.splitlines()[1]
    return [(int(number), i) for i, number in enumerate(line.split(",")) if number != "x"]
