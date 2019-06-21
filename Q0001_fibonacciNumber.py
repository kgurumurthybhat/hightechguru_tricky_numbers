# Solution in Python Fibonacci number.
cache_dict = {}


def fibonacci(n):
    if n in cache_dict:
        return cache_dict[n]
    if n == 0:
        return 1
    if n <= 2:
        return n
    else:
        result = fibonacci(n-1)+fibonacci(n-2)
        cache_dict[n] = result

    return result


nums = int(input('Enter a number, will print fibonacci numbers till that number: '))
for n in range(nums):
    print(n+1, '-', fibonacci(n))

fib = fibonacci(n)
print(n+1, '-', len(str(fib)), fib)