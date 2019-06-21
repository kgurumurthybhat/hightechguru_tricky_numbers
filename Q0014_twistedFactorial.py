# Python solution for Twisted Factorial
fact = {}
def twistedFactorial(n):
    if n in fact: return fact[n]
    if n==1: return 1
    else:
        fact[n] = (twistedFactorial(n-1) * n -1)
        return fact[n]


print(twistedFactorial(50))