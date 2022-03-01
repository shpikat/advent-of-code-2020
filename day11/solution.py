from typing import List

FLOOR = "."
SEAT = "L"
OCCUPIED = "#"


def part1(input_data: str) -> int:
    layout = read_seats_layout(input_data)

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
                    count_upper = upper_row[left:right].count(OCCUPIED)
                    count_this = row[left:right].count(OCCUPIED)
                    count_lower = lower_row[left:right].count(OCCUPIED)
                    occupied_count = count_upper + count_this + count_lower
                    if cursor == SEAT and occupied_count == 0:
                        new_row[seat_number] = OCCUPIED
                        should_run = True
                    elif cursor == OCCUPIED and occupied_count >= 5:
                        # occupied count includes self, hence 5
                        new_row[seat_number] = SEAT
                        should_run = True
            new_layout.append(new_row)
        layout = new_layout

    return sum((line.count(OCCUPIED) for line in layout))


def part2(input_data: str) -> int:
    layout = read_seats_layout(input_data)

    vectors = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

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


def read_seats_layout(input_data: str) -> List[List[str]]:
    return [list(line.rstrip()) for line in input_data.splitlines()]
