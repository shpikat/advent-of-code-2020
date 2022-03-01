from collections import deque


def part1(input_data: str) -> int:
    labeling = input_data
    circle = deque((int(ch) for ch in labeling), len(labeling))

    for i in range(100):
        current = circle.popleft()
        circle.append(current)
        picked_up = (
            circle.popleft(),
            circle.popleft(),
            circle.popleft(),
        )
        destination = current - 1 or circle.maxlen
        while destination in picked_up:
            destination -= 1
            if destination == 0:
                destination = circle.maxlen

        index = circle.index(destination)
        for value in reversed(picked_up):
            circle.insert(index + 1, value)

    circle.rotate(-circle.index(1))
    return int("".join(str(i) for i in circle)[1:])


def part2(input_data: str) -> int:
    labeling = input_data
    total_cups = 1_000_000
    moves = 10_000_000

    next_values = [i + 1 for i in range(total_cups + 1)]

    current = 0
    for character in labeling:
        value = int(character)
        next_values[current] = value
        current = value
    next_values[current] = len(labeling) + 1
    next_values[total_cups] = next_values[0]

    current = 0
    for i in range(moves):
        current = next_values[current]
        picked_up1 = next_values[current]
        picked_up2 = next_values[picked_up1]
        picked_up3 = next_values[picked_up2]
        next_values[current] = next_values[picked_up3]

        destination = current - 1 or total_cups
        while destination in (picked_up1, picked_up2, picked_up3):
            destination -= 1
            if destination == 0:
                destination = total_cups

        next_values[picked_up3] = next_values[destination]
        next_values[destination] = picked_up1

    cup1 = next_values[1]
    cup2 = next_values[cup1]
    return cup1 * cup2
