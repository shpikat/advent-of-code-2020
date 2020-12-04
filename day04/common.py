from typing import List, Dict


def read_input() -> List[Dict[str, str]]:
    with open("input", "r") as file:
        result = []
        accumulator = {}
        for line in file:
            if line == '\n':
                result.append(accumulator)
                accumulator = {}
            else:
                update = dict(entry.split(':') for entry in line.rstrip().split(' '))
                accumulator.update(update)
        if accumulator:
            result.append(accumulator)
        return result
