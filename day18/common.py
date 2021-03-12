from typing import List


def read_expressions() -> List[str]:
    with open("input", "r") as file:
        return file.read().replace(' ', '').split('\n')
