#Least Common Multiple - LCM
#Python:

i = 1
n = int(input("""
What is the smallest positive number that is evenly divisible by all of the numbers
from 1 to n. Enter n = ? 
"""))
for k in (range(1, n+1)):
    if i % k > 0:
        for j in range(1, n+1):
            if (i*j) % k == 0:
                i *= j
                break
print("""
The smallest +ve number that is evenly divisible by all of the numbers from 1 to {} = {}.
""".format(n, i))