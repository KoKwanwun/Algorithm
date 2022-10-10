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
    combList = set()

    for num in range(1, len(numbers)+1):
        combList |= set(map(int, map(''.join, permutations(numbers, num))))

    prime_list = prime_check(max(combList))

    for each in combList:
        if prime_list[each]:
            mlist.append(each)
        
    return len(mlist)