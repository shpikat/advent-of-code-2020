from day05.common import code_to_id, read_boarding_tickets


def solve(filename: str) -> int:
    boarding_tickets = read_boarding_tickets(filename)

    seats = (code_to_id(ticket) for ticket in boarding_tickets)
    max_seat = max(seats)

    return max_seat
