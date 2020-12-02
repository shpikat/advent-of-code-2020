import re
from typing import List, Tuple

line_parser = re.compile(r"(\d+)-(\d+) (\w): (\w+)")


def read_passwords() -> List[Tuple[int, int, str, str]]:
    with open("input", "r") as file:
        return [to_tuple(line.rstrip()) for line in file]


def to_tuple(line: str) -> Tuple[int, int, str, str]:
    groups = line_parser.fullmatch(line).groups()
    return int(groups[0]), int(groups[1]), groups[2], groups[3]
