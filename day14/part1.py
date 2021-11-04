from day14.common import mask_pattern, mem_pattern, read_program


def solve(filename: str) -> int:
    program = read_program(filename)

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
                zeroes = int(value.replace('X', '1'), 2)
                ones = int(value.replace('X', '0'), 2)
    return sum(mem.values())
