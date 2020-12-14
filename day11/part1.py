from day11.common import read_seats_layout, FLOOR, SEAT, OCCUPIED


def main():
    layout = read_seats_layout()

    empty_row = [FLOOR] * len(layout[0])

    should_run = True
    while should_run:
        should_run = False
        new_layout = []
        for row_number, row in enumerate(layout):
            upper_row = empty_row if row_number == 0 else layout[row_number - 1]
            lower_row = empty_row if row_number == len(layout) - 1 else layout[row_number + 1]
            new_row = row.copy()
            for seat_number, cursor in enumerate(row):
                if cursor != FLOOR:
                    left = max(seat_number - 1, 0)
                    right = min(seat_number + 2, len(row))
                    occupied_count = upper_row[left:right].count(OCCUPIED) \
                                     + row[left:right].count(OCCUPIED) \
                                     + lower_row[left:right].count(OCCUPIED)
                    if cursor == SEAT and occupied_count == 0:
                        new_row[seat_number] = OCCUPIED
                        should_run = True
                    elif cursor == OCCUPIED and occupied_count >= 5:
                        # occupied count includes self, hence 5
                        new_row[seat_number] = SEAT
                        should_run = True
            new_layout.append(new_row)
        layout = new_layout

    print(sum((line.count(OCCUPIED) for line in layout)))


if __name__ == "__main__":
    main()
