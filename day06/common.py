from typing import List


def read_answers() -> List[List[str]]:
    with open("input", "r") as file:
        return [group.split('\n') for group in file.read().split('\n\n')]
