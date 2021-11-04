import re
from typing import List

pattern = re.compile("e|se|sw|w|ne|nw")

moves = {
    'e': lambda x, y: (x + 1, y),
    'se': lambda x, y: (x, y - 1),
    'sw': lambda x, y: (x - 1, y - 1),
    'w': lambda x, y: (x - 1, y),
    'nw': lambda x, y: (x, y + 1),
    'ne': lambda x, y: (x + 1, y + 1),
}


def read_instructions(filename: str) -> List[List[str]]:
    with open(filename, "r") as file:
        return [pattern.findall(line) for line in file.read().split('\n') if line]
