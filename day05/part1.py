from day05.common import read_boarding_tickets, code_to_id


def main():
    boarding_tickets = read_boarding_tickets()

    seats = (code_to_id(ticket) for ticket in boarding_tickets)
    max_seat = max(seats)

    print(max_seat)


if __name__ == "__main__":
    main()
