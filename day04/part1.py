from day04.common import read_input


def main():
    passports = read_input()
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
    print(valid_count)


if __name__ == "__main__":
    main()
