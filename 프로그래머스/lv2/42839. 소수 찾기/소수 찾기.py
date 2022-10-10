from itertools import permutations

def prime_check(n):
    c = [False,False] + [True]*(n-1)
    for i in range(2, n+1):
        if c[i] == True:
            for j in range(2*i, n+1, i):
                c[j] = False
    return c

def solution(numbers):
    prime_list = prime_check(9999999)

    numbersList = list(numbers)

    mlist = []

    for num in range(1, len(numbers)+1):
        combList = list(permutations(numbers, num))

        for eachList in combList:
            eachComb = int(''.join(eachList))
            if eachComb in mlist:
                continue
            if prime_list[eachComb]:
                mlist.append(eachComb)
            
    return len(mlist)