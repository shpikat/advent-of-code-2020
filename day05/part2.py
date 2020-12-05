import operator
from typing import List

from day05.common import read_boarding_tickets, code_to_id


def main():
    boarding_tickets = read_boarding_tickets()

    seats = [code_to_id(ticket) for ticket in boarding_tickets]

    seats.sort()
    start_index = seats.index((seats[0] & 0b1111111000) + 0b1000)
    end_index = rindex(seats, (seats[-1] & 0b1111111000) - 1)
    for index, seat in enumerate(seats[start_index:end_index], seats[start_index]):
        if index != seat:
            print(index)
            break


def rindex(lst: List[int], value: int) -> int:
    return len(lst) - operator.indexOf(reversed(lst), value) - 1


if __name__ == "__main__":
    main()
