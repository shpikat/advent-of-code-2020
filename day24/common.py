import re
from typing import List

pattern = re.compile("e|se|sw|w|ne|nw")


def read_instructions() -> List[List[str]]:
    with open("input", "r") as file:
        return [pattern.findall(line) for line in file.read().split('\n') if line]
