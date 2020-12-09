from collections import deque

from day09.common import read_numbers, get_invalid_number


def main():
    numbers = read_numbers()

    target_sum = get_invalid_number(numbers)

    window = deque()
    window_sum = 0
    it = iter(numbers)
    while window_sum != target_sum:
        if window_sum > target_sum:
            window_sum -= window.popleft()
        elif window_sum < target_sum:
            number = next(it)
            window.append(number)
            window_sum += number
    print(min(window) + max(window))


if __name__ == "__main__":
    main()
