from typing import List


def read_answers(filename: str) -> List[List[str]]:
    with open(filename, "r") as file:
        return [group.rstrip().split('\n') for group in file.read().split('\n\n')]
