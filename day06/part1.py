from day06.common import read_answers


def main():
    answers = read_answers()
    total_count = sum(
        len(group_unique_answers) for group_unique_answers in
        (set(single_answer
             for person_answers in group_answers
             for single_answer in person_answers)
         for group_answers in answers))
    print(total_count)


if __name__ == "__main__":
    main()
