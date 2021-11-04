import re
from typing import List, Tuple

pattern = re.compile(r'^([^:]+): (\d+)-(\d+) or (\d+)-(\d+)$')


def read_rules_and_tickets(filename: str) -> Tuple[List[Tuple[str, int, int, int, int]], List[int], List[List[int]]]:
    with open(filename, "r") as file:
        sections = file.read().split('\n\n')
        return get_rules(sections[0].split('\n')), \
               get_your_ticket(sections[1].split('\n')), \
               get_nearby_tickets(sections[2].split('\n'))


def get_rules(lines: List[str]) -> List[Tuple[str, int, int, int, int]]:
    return [get_rule(line) for line in lines if line]


def get_rule(line: str) -> Tuple[str, int, int, int, int]:
    m = pattern.fullmatch(line)
    return m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))


def get_your_ticket(lines: List[str]) -> List[int]:
    return get_ticket(lines[1])


def get_nearby_tickets(lines: List[str]) -> List[List[int]]:
    return [get_ticket(line) for line in lines[1:] if line]


def get_ticket(line: str) -> List[int]:
    return [int(number) for number in line.split(',')]
