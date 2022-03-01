import re
from typing import Dict, List


def part1(input_data: str) -> int:
    passports = read_input(input_data)
    required_fields = {
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
        # allowed to skip
        # 'cid',
    }

    valid_count = 0
    for passport in passports:
        if required_fields.issubset({*passport}):
            valid_count += 1
    return valid_count


def part2(input_data: str) -> int:
    passports = read_input(input_data)
    validations = (
        ("byr", lambda x: 1920 <= int(x) <= 2002),
        ("iyr", lambda x: 2010 <= int(x) <= 2020),
        ("eyr", lambda x: 2020 <= int(x) <= 2030),
        ("hgt", lambda x: is_valid_hgt(x)),
        ("hcl", lambda x: re_hcl.fullmatch(x)),
        ("ecl", lambda x: x in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}),
        ("pid", lambda x: re_pid.fullmatch(x)),
    )

    valid_count = 0
    for passport in passports:
        if all(field in passport and is_valid(passport[field]) for field, is_valid in validations):
            valid_count += 1
    return valid_count


re_hgt = re.compile(r"^(\d+)(cm|in)$")
re_hcl = re.compile(r"^#[0-9a-f]{6}$")
re_pid = re.compile(r"^\d{9}$")


def is_valid_hgt(x: str) -> bool:
    match = re_hgt.fullmatch(x)
    if match:
        value, measurement = int(match.group(1)), match.group(2)
        if measurement == "cm":
            return 150 <= value <= 193
        elif measurement == "in":
            return 59 <= value <= 76
    return False


def read_input(input_data: str) -> List[Dict[str, str]]:
    return [dict(entry.split(":") for entry in group.split()) for group in input_data.split("\n\n")]
