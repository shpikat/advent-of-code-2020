from day02.common import read_passwords


def solve(filename: str) -> int:
    passwords = read_passwords(filename)

    valid_count = 0
    for (position1, position2, letter, password) in passwords:
        if (password[position1 - 1] == letter) != (password[position2 - 1] == letter):
            valid_count += 1
    return valid_count
