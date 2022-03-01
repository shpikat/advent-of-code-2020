import re
from typing import List, Tuple


def part1(input_data: str) -> int:
    passwords = read_passwords(input_data)

    valid_count = 0
    for (min_count, max_count, letter, password) in passwords:
        password_count = password.count(letter)
        if min_count <= password_count <= max_count:
            valid_count += 1
    return valid_count


def part2(input_data: str) -> int:
    passwords = read_passwords(input_data)

    valid_count = 0
    for (position1, position2, letter, password) in passwords:
        if (password[position1 - 1] == letter) != (password[position2 - 1] == letter):
            valid_count += 1
    return valid_count


line_parser = re.compile(r"(\d+)-(\d+) (\w): (\w+)")


def read_passwords(input_data: str) -> List[Tuple[int, int, str, str]]:
    return [to_tuple(line.rstrip()) for line in input_data.splitlines()]


def to_tuple(line: str) -> Tuple[int, int, str, str]:
    groups = line_parser.fullmatch(line).groups()
    return int(groups[0]), int(groups[1]), groups[2], groups[3]
