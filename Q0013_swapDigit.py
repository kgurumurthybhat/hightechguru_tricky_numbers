# Python solution for Swap Neighboring digit


def swapNeighbouringDigits(n):
    number = str(n)
    new_number = ''
    for i in range(1, len(number)):
        if i % 2 != 0:
            new_number += number[i] + number[i - 1]
    print(new_number)
    return int(new_number)


def swap_num_sum(s, e):
    res = 0
    for i in range(s, e + 1):
        res += swapNeighbouringDigits(i)
    return res


print(swap_num_sum(100000, 999999))
