#Python Solution Rotating Prime Number


def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int((n + 1) ** .5 + 1)):
            if n % i == 0:
                return False
    return True


def rotate_list(n):
    result = []
    new_num = str(n)
    for i in range(len(str(n))):
        new_num = new_num[1:] + new_num[0]
        if isPrime(int(new_num)):
            result.append(int(new_num))
        else:
            return False
    # print(result)
    return True


z = int(input('Enter upper limit number: '))
res_list = []
for i in range(z+1):
    if isPrime(i):
        if rotate_list(i):
            res_list.append(i)
count = len(res_list)
print('There are {} circular prime numbers, the list is {}'.format(count, res_list))