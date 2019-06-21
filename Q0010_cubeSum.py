# Python Solution for Add and Subtract of cubes

def cubeSum(n):
    s1 = 0
    s2 = 0
    for i in range(n+1):
        s1 += i**3
        s2 += i
    return s2**3 - s1

n = 1000
print(cubeSum(n))