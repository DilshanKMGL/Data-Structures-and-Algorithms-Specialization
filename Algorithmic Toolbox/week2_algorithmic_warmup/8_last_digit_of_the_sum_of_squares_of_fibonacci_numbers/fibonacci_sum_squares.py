# Uses python3


def fibonacci_sum_squares_naive(n):
    fib = [0, 1]

    for _ in range(2, 60):
        fib.append((fib[-1] + fib[-2]) % 10)

    m = (n + 1) % 60
    n %= 60

    if m < n:
        m += 60

    return (fib[m % 60] * fib[n % 60]) % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_naive(n))
