from day11.common import FLOOR, OCCUPIED, SEAT, read_seats_layout


def solve(filename: str) -> int:
    layout = read_seats_layout(filename)

    vectors = [(-1, -1), (0, -1), (1, -1),
               (-1, 0), (1, 0),
               (-1, 1), (0, 1), (1, 1)]

    should_run = True
    while should_run:
        should_run = False
        new_layout = []
        for row_number, row in enumerate(layout):
            new_row = row.copy()
            for seat_number, cursor in enumerate(row):
                if cursor != FLOOR:
                    occupied_count = 0
                    for (dx, dy) in vectors:
                        x = seat_number + dx
                        y = row_number + dy
                        while 0 <= x < len(row) and 0 <= y < len(layout):
                            position_under_check = layout[y][x]
                            if position_under_check == SEAT:
                                break
                            if position_under_check == OCCUPIED:
                                occupied_count += 1
                                break
                            x += dx
                            y += dy

                    if cursor == SEAT and occupied_count == 0:
                        new_row[seat_number] = OCCUPIED
                        should_run = True
                    elif cursor == OCCUPIED and occupied_count >= 5:
                        new_row[seat_number] = SEAT
                        should_run = True
            new_layout.append(new_row)
        layout = new_layout

    return sum((line.count(OCCUPIED) for line in layout))
