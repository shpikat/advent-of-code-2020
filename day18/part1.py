from day18.common import read_expressions


def main():
    expressions = read_expressions()
    print(sum(solve(expression) for expression in expressions if expression))


def solve(expression: str) -> int:
    stack = []
    accumulator = 0
    operand = 0
    in_operand = False
    operator = None
    operators = {
        '+': lambda a, b: a + b,
        '*': lambda a, b: a * b,
    }
    for ch in expression:
        if '0' <= ch <= '9':
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
            if ch == '(':
                if operator:
                    stack.append((accumulator, operator))
                    operator = None
                else:
                    stack.append((0, None))
            elif ch == ')':
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


if __name__ == "__main__":
    main()
