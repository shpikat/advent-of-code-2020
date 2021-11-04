from collections import deque

from day23.common import read_labeling


def solve(filename: str) -> int:
    labeling = read_labeling(filename)
    circle = deque((int(ch) for ch in labeling), len(labeling))

    for i in range(100):
        current = circle.popleft()
        circle.append(current)
        picked_up = (circle.popleft(), circle.popleft(), circle.popleft(),)
        destination = current - 1 or circle.maxlen
        while destination in picked_up:
            destination -= 1
            if destination == 0:
                destination = circle.maxlen

        index = circle.index(destination)
        for value in reversed(picked_up):
            circle.insert(index + 1, value)

    circle.rotate(-circle.index(1))
    return int(''.join(str(i) for i in circle)[1:])
