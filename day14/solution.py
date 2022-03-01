import itertools
import re
from typing import List, Tuple


def part1(input_data: str) -> int:
    program = read_program(input_data)

    mem = {}
    zeroes = -1
    ones = 0
    for instruction in program:
        match = mem_pattern.fullmatch(instruction)
        if match:
            address = int(match.group(1))
            value = int(match.group(2))
            mem[address] = (value & zeroes) | ones
        else:
            match = mask_pattern.fullmatch(instruction)
            if match:
                value = match.group(1)
                zeroes = int(value.replace("X", "1"), 2)
                ones = int(value.replace("X", "0"), 2)
    return sum(mem.values())


def part2(input_data: str) -> int:
    program = read_program(input_data)

    mem = {}
    masks = []
    for instruction in program:
        match = mem_pattern.fullmatch(instruction)
        if match:
            base_address = int(match.group(1))
            value = int(match.group(2))
            mem.update((((base_address & zeroes) | ones), value) for zeroes, ones in masks)
        else:
            match = mask_pattern.fullmatch(instruction)
            if match:
                value = list(match.group(1))
                base_zeroes = ["1"] * len(value)
                base_ones = ["1" if ch == "1" else "0" for ch in value]
                indices = [i for i, ch in enumerate(value) if ch == "X"]
                masks = [
                    create_masks_tuple(base_zeroes.copy(), base_ones.copy(), digits, indices)
                    for digits in itertools.product("01", repeat=len(indices))
                ]
    return sum(mem.values())


def create_masks_tuple(
    zeroes: List[str],
    ones: List[str],
    digits: Tuple[any],
    indices: List[int],
) -> Tuple[int, int]:
    for index, digit in zip(indices, digits):
        zeroes[index] = digit
        ones[index] = digit
    return binary_to_int(zeroes), binary_to_int(ones)


def binary_to_int(mask: List[str]) -> int:
    return int("".join(mask), 2)


mask_pattern = re.compile(r"^mask = (\w+)$")
mem_pattern = re.compile(r"^mem\[(\d+)] = (\d+)$")


def read_program(input_data: str) -> List[str]:
    return input_data.splitlines()
