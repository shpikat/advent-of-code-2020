from day02.common import read_passwords


def solve(filename: str) -> int:
    passwords = read_passwords(filename)

    valid_count = 0
    for (min_count, max_count, letter, password) in passwords:
        password_count = password.count(letter)
        if min_count <= password_count <= max_count:
            valid_count += 1
    return valid_count
