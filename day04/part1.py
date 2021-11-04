from day04.common import read_input


def solve(filename: str) -> int:
    passports = read_input(filename)
    required_fields = {
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        # allowed to skip
        # 'cid',
    }

    valid_count = 0
    for passport in passports:
        if required_fields.issubset({*passport}):
            valid_count += 1
    return valid_count
