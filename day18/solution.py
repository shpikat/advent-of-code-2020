from typing import List


operators = {
    "+": lambda a, b: a + b,
    "*": lambda a, b: a * b,
}


def part1(input_data: str) -> int:
    expressions = read_expressions(input_data)
    return sum(solve_with_same_precedence(expression) for expression in expressions if expression)


def solve_with_same_precedence(expression: str) -> int:
    stack = []
    accumulator = 0
    operand = 0
    in_operand = False
    operator = None
    for ch in expression:
        if "0" <= ch <= "9":
            in_operand = True
            operand = operand * 10 + int(ch)
        else:
            if in_operand:
                if operator:
                    operand = operator(accumulator, operand)
                    operator = None
                accumulator = operand
                operand = 0
                in_operand = False
            if ch == "(":
                if operator:
                    stack.append((accumulator, operator))
                    operator = None
                else:
                    stack.append((0, None))
            elif ch == ")":
                if stack:
                    operand, operator = stack.pop()
                    if operator:
                        accumulator = operator(accumulator, operand)
                        operand = 0
                        operator = None
            else:
                operator = operators[ch]

    if operator:
        accumulator = operator(accumulator, operand)

    return accumulator


def part2(input_data: str) -> int:
    expressions = read_expressions(input_data)
    return sum(
        solve_with_different_precedence(expression) for expression in expressions if expression
    )


def solve_with_different_precedence(expression: str) -> int:
    operands_stack = []
    operations_stack = []
    operand = 0
    in_operand = False
    for ch in expression:
        if "0" <= ch <= "9":
            in_operand = True
            operand = operand * 10 + int(ch)
        else:
            if in_operand:
                operands_stack.append(operand)
                operand = 0
                in_operand = False

            if ch == "(":
                operations_stack.append(ch)
            elif ch == ")":
                while True:
                    operator = operations_stack.pop()
                    if operator == "(":
                        break
                    do_operation(operands_stack, operator)
            else:
                while operations_stack and is_precedence_same_or_higher(operations_stack[-1], ch):
                    do_operation(operands_stack, operations_stack.pop())
                operations_stack.append(ch)

    # Could've been simplified into a parser as `elif ch == '='` case, if the expression ended with '='
    if in_operand:
        operands_stack.append(operand)
    while operations_stack:
        do_operation(operands_stack, operations_stack.pop())

    return operands_stack.pop()


def do_operation(operands_stack: List[int], operator: str) -> None:
    operation = operators[operator]
    result = operation(operands_stack.pop(), operands_stack.pop())
    operands_stack.append(result)


def is_precedence_same_or_higher(o1: str, o2: str) -> bool:
    return o1 != "(" and (o1 == o2 or o1 == "+")


def read_expressions(input_data: str) -> List[str]:
    return input_data.replace(" ", "").splitlines()
