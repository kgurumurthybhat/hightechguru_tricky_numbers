# Python solution for Collatz Conjecture.


c_dict = {}


def main():
    current_count = 1
    max_counter = 0
    start_num = 1
    start_num_big = 1
    n = int(input("Enter number to check: "))
    for i in range(1, n + 1):
        start_num, current_count = max_count(i)
        if current_count > max_counter:
            max_counter = current_count
            start_num_big = start_num
        # print(str(i*100/n) + "% complete")
    print(start_num_big, max_counter)


def max_count(n):
    global c_dict
    if n in c_dict:
        return n, c_dict[n]
    # n = int(input("Enter the number for Collatz sequence: "))
    colatz_list = [n]
    next_num = n
    while (next_num >= 2):
        if (next_num % 2 == 0):
            next_num = int(next_num / 2)
        else:
            next_num = int((next_num * 3) + 1)
        colatz_list.append(next_num)
    # print(len(colatz_list), colatz_list)
    c_dict[n] = len(colatz_list)
    # print(c_dict, colatz_list)
    return (colatz_list[0], len(colatz_list))


main()