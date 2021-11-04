from typing import List


def read_boarding_tickets(filename: str) -> List[str]:
    with open(filename, "r") as file:
        return [line.rstrip() for line in file.readlines()]


def code_to_id(code: str) -> int:
    # it all comes to bits 4-11 are row number and bits 0-3 are row seat number
    digits = code.translate({ord('F'): '0', ord('B'): '1', ord('L'): '0', ord('R'): '1'})
    return int(digits, 2)
