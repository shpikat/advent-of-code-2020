from typing import List


def read_answers() -> List[List[str]]:
    with open("input", "r") as file:
        result = []
        accumulator = []
        for line in file:
            if line == '\n':
                result.append(accumulator)
                accumulator = []
            else:
                accumulator.append(line.rstrip())
        if accumulator:
            result.append(accumulator)
        return result
