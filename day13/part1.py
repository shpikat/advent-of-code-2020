from typing import List, Tuple


def read_schedule(filename: str) -> Tuple[int, List[int]]:
    with open(filename, "r") as file:
        timestamp = int(file.readline())
        schedule = [int(number) for number in file.readline().split(',') if number != 'x']
        return timestamp, schedule


def solve(filename: str) -> int:
    departure, schedule = read_schedule(filename)

    min_wait, earliest_bus = min((
        (((departure - 1) // bus + 1) * bus - departure, bus)
        for bus in schedule))
    return min_wait * earliest_bus
