import re
from typing import List

mask_pattern = re.compile(r'^mask = (\w+)$')
mem_pattern = re.compile(r'^mem\[(\d+)] = (\d+)$')


def read_program(filename: str) -> List[str]:
    with open(filename, "r") as file:
        return file.read().split('\n')
