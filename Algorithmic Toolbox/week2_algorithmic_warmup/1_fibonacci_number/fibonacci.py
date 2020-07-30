# Uses python3


def calc_fib(n):
    previous = 0
    current = 1

    if n < 2:
        return n
    else:
        for _ in range(2, n):
            previous, current = current, previous + current
        return previous + current


n = int(input())
print(calc_fib(n))
