import re
from typing import List, Tuple

parser_bag = re.compile(r"(\w+ \w+) bags contain ")
parser_contains = re.compile(r"(\d+) (\w+ \w+) bags?(, )?")


def read_rules(filename: str) -> List[Tuple[str, List[Tuple[int, str]]]]:
    with open(filename, "r") as file:
        return [parse(rule.strip()) for rule in file.readlines()]


def parse(rule: str) -> Tuple[str, List[Tuple[int, str]]]:
    bag = parser_bag.match(rule).group(1)
    contains = [(int(match.group(1)), match.group(2))
                for match in parser_contains.finditer(rule, len(bag))]
    return bag, contains
