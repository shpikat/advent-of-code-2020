from day05.common import read_boarding_tickets, code_to_id


def main():
    boarding_tickets = read_boarding_tickets()

    seats = [code_to_id(ticket) for ticket in boarding_tickets]

    seats.sort()
    starting_seat = (seats[0] & 0b1111111000) + 0b1000
    ending_seat = seats[-1] & 0b1111111000
    # may as well be just 0, as the task says there are seats in front
    previous_seat = starting_seat - 1
    for seat in seats:
        if starting_seat <= seat < ending_seat:
            expected_seat = previous_seat + 1
            if expected_seat != seat:
                print(expected_seat)
                break
        previous_seat = seat


if __name__ == "__main__":
    main()
