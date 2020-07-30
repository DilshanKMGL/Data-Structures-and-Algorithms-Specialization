# Uses python3


def fibonacci_partial_sum_naive(m, n):
    fib = [0, 1]
    for _ in range(2, 60):
        fib.append(fib[-1] + fib[-2])
    m %= 60
    n %= 60

    if n < m:
        n += 60

    sum = 0

    for i in range(m, n + 1):
        sum += fib[i%60]
    return sum % 10


if __name__ == '__main__':
    input = input()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
