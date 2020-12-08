from day08.common import read_program, run_with_loop_detection


def main():
    program = read_program()

    for index, (command, argument) in enumerate(program):
        if command == 'jmp':
            patched_command = 'nop'
        elif command == 'nop':
            patched_command = 'jmp'
        else:
            continue
        patched_program = program.copy()
        patched_program[index] = patched_command, argument
        accumulator, is_success = run_with_loop_detection(patched_program)
        if is_success:
            print(accumulator)
            break


if __name__ == "__main__":
    main()
