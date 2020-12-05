from day05.common import read_boarding_tickets


def main():
    boarding_tickets = read_boarding_tickets()

    seats = (code_to_id(ticket) for ticket in boarding_tickets)
    max_seat = max(seats)

    print(max_seat)


def code_to_id(code: str) -> int:
    # it all comes to bits 4-11 are row number and bits 0-3 are row seat number
    digits = code.translate({ord('F'): '0', ord('B'): '1', ord('L'): '0', ord('R'): '1'})
    return int(digits, 2)


if __name__ == "__main__":
    main()
