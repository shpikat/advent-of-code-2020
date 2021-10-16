import re
from dataclasses import dataclass
from typing import List

line_parser = re.compile(r"([^(]+) \(contains ([^)]+)\)")


@dataclass(frozen=True)
class Food:
    ingredients: List[str]
    allergens: List[str]


def read_foods() -> List[Food]:
    with open("input", "r") as file:
        return [parse_food(line) for line in file.read().rstrip().split('\n')]


def parse_food(line: str) -> Food:
    groups = line_parser.fullmatch(line).groups()
    return Food(groups[0].split(' '), groups[1].split(', '))
