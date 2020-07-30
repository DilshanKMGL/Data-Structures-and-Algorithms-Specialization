# Uses python3


def lcm_naive(a, b):

    if b == 0:
        return a
    a_prime = a % b
    return lcm_naive(b, a_prime)


if __name__ == '__main__':
    input = input()
    a, b = map(int, input.split())
    print(int(a*b/lcm_naive(a, b)))
