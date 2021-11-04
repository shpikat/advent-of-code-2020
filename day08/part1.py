from day08.common import read_program, run_with_loop_detection


def solve(filename: str) -> int:
    program = read_program(filename)

    accumulator, _ = run_with_loop_detection(program)
    return accumulator
