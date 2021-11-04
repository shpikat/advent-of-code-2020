import itertools
from typing import List, Tuple

from day14.common import mask_pattern, mem_pattern, read_program


def solve(filename: str) -> int:
    program = read_program(filename)

    mem = {}
    masks = []
    for instruction in program:
        match = mem_pattern.fullmatch(instruction)
        if match:
            base_address = int(match.group(1))
            value = int(match.group(2))
            mem.update((((base_address & zeroes) | ones), value)
                       for zeroes, ones in masks)
        else:
            match = mask_pattern.fullmatch(instruction)
            if match:
                value = list(match.group(1))
                base_zeroes = ['1'] * len(value)
                base_ones = ['1' if ch == '1' else '0' for ch in value]
                indices = [i for i, ch in enumerate(value) if ch == 'X']
                masks = [create_masks_tuple(base_zeroes.copy(), base_ones.copy(), digits, indices)
                         for digits in itertools.product('01', repeat=len(indices))]
    return sum(mem.values())


def create_masks_tuple(zeroes: List[str], ones: List[str], digits: Tuple[any], indices: List[int]) -> Tuple[int, int]:
    for index, digit in zip(indices, digits):
        zeroes[index] = digit
        ones[index] = digit
    return binary_to_int(zeroes), binary_to_int(ones)


def binary_to_int(mask: List[str]) -> int:
    return int(''.join(mask), 2)
