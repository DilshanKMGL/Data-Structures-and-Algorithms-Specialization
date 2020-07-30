# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_num1_i = 0
    max_num1 = 0
    max_num2 = 0

    for i in range(n):
        if numbers[i] > max_num1:
            max_num1 = numbers[i]
            max_num1_i = i
    for i in range(n):
        if (i != max_num1_i) and (max_num1 >= numbers[i] > max_num2):
            max_num2 = numbers[i]
    return max_num1*max_num2


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
