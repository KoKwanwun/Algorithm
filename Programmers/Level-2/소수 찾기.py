from itertools import permutations

# 에라토스테네스의 체(인덱스가 소수면 True)
def prime_check(n):
    c = [False,False] + [True]*(n-1)
    for i in range(2, n+1):
        if c[i] == True:
            for j in range(2*i, n+1, i):
                c[j] = False
    return c


def solution(numbers):
    mlist = []
    combSet = set()

    # for문을 돌면서 순열을 사용하여 경우의 수를 만들고, 이후 set으로 중복제거하여 합집합(|=)
    for num in range(1, len(numbers)+1):
        combSet |= set(map(int, map(''.join, permutations(list(numbers), num))))

    # 경우의 수의 최대값만큼 소수 리스트 생성
    prime_list = prime_check(max(combSet))

    # 소수라면 mlist에 넣기
    for each in combSet:
        if prime_list[each]:
            mlist.append(each)
        
    return len(mlist)