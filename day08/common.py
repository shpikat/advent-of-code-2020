from typing import List, Tuple


def read_program(filename: str) -> List[Tuple[str, int]]:
    with open(filename, "r") as file:
        return [parse(line.rstrip()) for line in file.readlines()]


def parse(line: str) -> Tuple[str, int]:
    command, value = line.split()
    return command, int(value)


def run(program: List[Tuple[str, int]]) -> Tuple[int, int]:
    accumulator = offset = 0
    operations = {
        'acc': lambda arg, off, acc: (off + 1, acc + arg),
        'jmp': lambda arg, off, acc: (off + arg, acc),
        'nop': lambda arg, off, acc: (off + 1, acc),
    }
    while True:
        command, argument = program[offset]
        offset, accumulator = operations[command](argument, offset, accumulator)
        yield offset, accumulator


def run_with_loop_detection(program: List[Tuple[str, int]]) -> Tuple[int, bool]:
    visited_offsets = {0}
    for offset, accumulator in run(program):
        if offset >= len(program):
            return accumulator, True
        elif offset in visited_offsets:
            return accumulator, False
        visited_offsets.add(offset)
