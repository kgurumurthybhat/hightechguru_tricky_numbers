                #Natural number multiples
                #Solution to Q0008
def multiples(n, m, k):
    mult = []
    for i in range(1, k):
        if i % n == 0 or i % m == 0:
            mult.append(i)

    return sum(mult)


n = 7
m = 9
k = 1000000
print(multiples(n, m, k))