from typing import List, Tuple


def part1(input_data: str) -> int:
    program = read_program(input_data)

    accumulator, _ = run_with_loop_detection(program)
    return accumulator


def part2(input_data: str) -> int:
    program = read_program(input_data)

    for index, (command, argument) in enumerate(program):
        if command == "jmp":
            patched_command = "nop"
        elif command == "nop":
            patched_command = "jmp"
        else:
            continue
        patched_program = program.copy()
        patched_program[index] = patched_command, argument
        accumulator, is_success = run_with_loop_detection(patched_program)
        if is_success:
            return accumulator


def read_program(input_data: str) -> List[Tuple[str, int]]:
    return [parse(line.rstrip()) for line in input_data.splitlines()]


def parse(line: str) -> Tuple[str, int]:
    command, value = line.split()
    return command, int(value)


def run(program: List[Tuple[str, int]]) -> Tuple[int, int]:
    accumulator = offset = 0
    operations = {
        "acc": lambda arg, off, acc: (off + 1, acc + arg),
        "jmp": lambda arg, off, acc: (off + arg, acc),
        "nop": lambda arg, off, acc: (off + 1, acc),
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
