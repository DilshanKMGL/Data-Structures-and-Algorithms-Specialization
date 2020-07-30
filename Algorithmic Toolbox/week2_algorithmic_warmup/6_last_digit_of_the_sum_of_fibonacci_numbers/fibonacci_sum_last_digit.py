# Uses python3


def fibonacci_sum_naive(n):
    sum = 1
    if n < 2:
        return n

    n = (n + 2) % 60
    previous = 0
    current = 1
    for _ in range(2, n + 1):
        previous, current = current, (previous + current) % 10
    if current == 0:
        return 9
    else:
        return current - 1


if __name__ == '__main__':
    input = input()
    n = int(input)
    print(fibonacci_sum_naive(n))
