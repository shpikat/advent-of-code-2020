from typing import List


def read_boarding_tickets() -> List[str]:
    with open("input", "r") as file:
        return [line.rstrip() for line in file.readlines()]
