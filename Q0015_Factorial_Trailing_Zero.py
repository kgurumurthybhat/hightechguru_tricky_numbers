# Python solution for Factorial Trailing Zeros


d = {}


def f(n):
    if n in d:
        return d[n]
    if n < 3:
        return n
    d[n] = n * f(n - 1)
    return d[n]


def factorialTrailingZeros(n):
    r = str(f(n))
    c = 0
    for digit in r[::-1]:
        if int(digit) == 0:
            c += 1
        else:
            break
    print("{}! = {}".format(n, f(n)))
    return c


n = int(input("Enter a number: "))
print("Trailing zeros in {}! = {}".format(n, factorialTrailingZeros(n)))