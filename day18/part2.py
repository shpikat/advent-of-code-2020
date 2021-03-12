from typing import List

from day18.common import read_expressions


def main():
    expressions = read_expressions()
    print(sum(solve(expression) for expression in expressions if expression))


operators = {
    '+': lambda a, b: a + b,
    '*': lambda a, b: a * b,
}


def solve(expression: str) -> int:
    operands_stack = []
    operations_stack = []
    operand = 0
    in_operand = False
    for ch in expression:
        if '0' <= ch <= '9':
            in_operand = True
            operand = operand * 10 + int(ch)
        else:
            if in_operand:
                operands_stack.append(operand)
                operand = 0
                in_operand = False

            if ch == '(':
                operations_stack.append(ch)
            elif ch == ')':
                while True:
                    operator = operations_stack.pop()
                    if operator == '(':
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
    return o1 != '(' and (o1 == o2 or o1 == '+')


if __name__ == "__main__":
    main()
