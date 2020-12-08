from day08.common import read_program, run_with_loop_detection


def main():
    program = read_program()

    accumulator, _ = run_with_loop_detection(program)
    print(accumulator)


if __name__ == "__main__":
    main()
