from collections import defaultdict

from day07.common import read_rules


def main():
    rules = read_rules()

    index = defaultdict(set)
    for bag, contains in rules:
        for count, contained in contains:
            index[contained].add(bag)

    result = set()
    current_iteration = set(index["shiny gold"])
    while current_iteration:
        result |= current_iteration
        iteration_result = set(contained
                               for bag in current_iteration
                               for contained in index[bag])
        current_iteration = iteration_result - result
    print(len(result))


if __name__ == "__main__":
    main()
