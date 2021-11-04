from typing import List


def read_expressions(filename: str) -> List[str]:
    with open(filename, "r") as file:
        return file.read().replace(' ', '').split('\n')
