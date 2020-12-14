from typing import List, Tuple


def read_schedule() -> Tuple[int, List[int]]:
    with open("input", "r") as file:
        timestamp = int(file.readline())
        schedule = [int(number) for number in file.readline().split(',') if number != 'x']
        return timestamp, schedule


def main():
    departure, schedule = read_schedule()

    min_wait, earliest_bus = min((
        (((departure - 1) // bus + 1) * bus - departure, bus)
        for bus in schedule))
    print(min_wait * earliest_bus)


if __name__ == "__main__":
    main()
