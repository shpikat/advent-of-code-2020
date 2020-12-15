import re
from typing import List

mask_pattern = re.compile(r'^mask = (\w+)$')
mem_pattern = re.compile(r'^mem\[(\d+)] = (\d+)$')


def read_program() -> List[str]:
    with open("input", "r") as file:
        return file.read().split('\n')
