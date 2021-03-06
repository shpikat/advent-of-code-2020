from typing import List, Tuple


def read_requirements() -> List[Tuple[int, int]]:
    with open("input", "r") as file:
        file.readline()
        return [(int(number), i)
                for i, number in enumerate(file.readline().split(','))
                if number != 'x']


def main():
    requirements = read_requirements()

    timestamp = 0
    step = 1
    for interval, gap in requirements:
        while timestamp < interval:
            timestamp += step
        while (timestamp + gap) % interval != 0:
            timestamp += step
        step *= interval
    print(timestamp)


if __name__ == "__main__":
    main()
