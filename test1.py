"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].

"""

def solution(A):

    A.sort()
    if A[-1] <= 0:
        return 1
    if len(A) < 2:
        if A[0] > 1:
            return 1
        else:
            return A[0] + 1
    for i in range(1, len(A)):
        if A[i] > A[i-1] + 1:
            if A[i-1] > 0:
                return A[i-1] + 1
            elif A[i] > 1:
                return 1
    return A[i] + 1


A = [1, 3, 6, 4, 1, 2]
A = [1,1,1,1,1,1,1]
A= [0,0,0,0,00,-1,999999]
A = [1,3,2,5,4,6,5,7,9,8,10, 12, 14,13, 15]

A = [4,5,6,7]
print(solution(A))