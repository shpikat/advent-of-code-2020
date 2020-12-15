from day14.common import read_program, mask_pattern, mem_pattern


def main():
    program = read_program()

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
    print(sum(mem.values()))


if __name__ == "__main__":
    main()
