# Python Solution for Power Summation
def self_power(n):
    result = 0
    for i in range(1, n+1):
        result += i**i
    return str(result)[-20:]


n = int(input("Enter a number: "))
print(self_power(n))