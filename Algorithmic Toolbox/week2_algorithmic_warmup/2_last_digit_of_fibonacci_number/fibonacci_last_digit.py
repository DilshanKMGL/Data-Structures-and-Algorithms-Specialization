# Uses python3


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(2, n):
        previous, current = current, (previous + current) % 10
        # print(i,"previous",previous, "current",current)
    return (current + previous) % 10


if __name__ == '__main__':
    input = input()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
