# Python solution - Prime Number Sum


def isPrime(n):
    if n == 1:
        return False
    if n < 4:
        return True
    for i in range(2, int(n**0.5 + 1)):
        if n%i == 0:
            return False
    return True


def primeSum(counter, max_count):
    count = 0
    i = 1
    res = 0
    while count < max_count:
        if isPrime(i):
            count +=1
            if count in counter:
                res += i
        i += 1
    return res


counter = [10, 1000, 100000]
max_count = max(counter) + 1
print(primeSum(counter, max_count))