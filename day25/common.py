from typing import Tuple

SUBJECT = 7
DIVISOR = 20201227


def read_public_keys(filename: str) -> Tuple[int, int]:
    with open(filename, "r") as file:
        return readline(file), readline(file)


def readline(file) -> int:
    return int(file.readline().strip())
