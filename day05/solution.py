import operator
from typing import List


def part1(input_data: str) -> int:
    boarding_tickets = read_boarding_tickets(input_data)

    seats = (code_to_id(ticket) for ticket in boarding_tickets)
    max_seat = max(seats)

    return max_seat


def part2(input_data: str) -> int:
    boarding_tickets = read_boarding_tickets(input_data)

    seats = [code_to_id(ticket) for ticket in boarding_tickets]

    seats.sort()
    start_index = seats.index((seats[0] & 0b1111111000) + 0b1000)
    end_index = rindex(seats, (seats[-1] & 0b1111111000) - 1)

    return find_gap_in_sequence(seats[start_index:end_index])


def rindex(lst: List[int], value: int) -> int:
    return len(lst) - operator.indexOf(reversed(lst), value) - 1


def find_gap_in_sequence(lst: List[int]) -> int:
    index_delta = lst[0]
    low, high = 0, len(lst) - 1
    while high - low > 1:
        median = low + ((high - low) // 2)
        if lst[median] == median + index_delta:
            low = median
        else:
            high = median
    else:
        return lst[low] + 1 if lst[low] == low + index_delta else lst[low]


def read_boarding_tickets(input_data: str) -> List[str]:
    return [line.rstrip() for line in input_data.splitlines()]


translation = {
    ord("F"): "0",
    ord("B"): "1",
    ord("L"): "0",
    ord("R"): "1",
}


def code_to_id(code: str) -> int:
    # it all comes to bits 4-11 are row number and bits 0-3 are row seat number
    digits = code.translate(translation)
    return int(digits, 2)
