# Uses python3
import sys


def pisano(m):
    previous = 0
    current = 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1


def get_fibonacci_huge_naive(n, m):
    pis = pisano(m)

    n %= pis
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        previous = 0
        current = 1
        for i in range(2, n):
            previous, current = current, previous + current
        return (previous + current) % m


if __name__ == '__main__':
    input = input()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
