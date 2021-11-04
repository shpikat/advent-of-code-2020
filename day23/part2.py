from day23.common import read_labeling

TOTAL_CUPS = 1_000_000
MOVES = 10_000_000


def solve(filename: str) -> int:
    labeling = read_labeling(filename)

    next_values = [i + 1 for i in range(TOTAL_CUPS + 1)]

    current = 0
    for character in labeling:
        value = int(character)
        next_values[current] = value
        current = value
    next_values[current] = len(labeling) + 1
    next_values[TOTAL_CUPS] = next_values[0]

    current = 0
    for i in range(MOVES):
        current = next_values[current]
        picked_up1 = next_values[current]
        picked_up2 = next_values[picked_up1]
        picked_up3 = next_values[picked_up2]
        next_values[current] = next_values[picked_up3]

        destination = current - 1 or TOTAL_CUPS
        while destination in (picked_up1, picked_up2, picked_up3):
            destination -= 1
            if destination == 0:
                destination = TOTAL_CUPS

        next_values[picked_up3] = next_values[destination]
        next_values[destination] = picked_up1

    cup1 = next_values[1]
    cup2 = next_values[cup1]
    return cup1 * cup2
