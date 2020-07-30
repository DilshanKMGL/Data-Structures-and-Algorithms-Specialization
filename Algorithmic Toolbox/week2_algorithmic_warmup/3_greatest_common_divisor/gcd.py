# Uses python3


def gcd_naive(a, b):
    if b == 0:
        return a
    a_prime = a % b
    return gcd_naive(b, a_prime)


if __name__ == "__main__":
    input = [int(x) for x in input().split()]
    print(gcd_naive(input[0], input[1]))
