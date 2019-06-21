# Solution in Python - Q0004 Digit Sum.


def digitSum():
    p = int(input('Enter base number: '))
    q = int(input('Enter power number: '))
    n = str(p**q)
    dSum = 0
    for digit in range(len(n)):
       dSum += int(n[digit])
    return dSum


print("Sum of digits = {}".format(digitSum()))


