n, m = map(int, input().split())
mlist = [[] for _ in range(26)]
root = [1] * 26

# 마약공급책과 공급대상을 정수로 바꿔 리스트에 넣기
# root는 원산지
for _ in range(m):
    start, end = input().split()
    mlist[ord(start)-65].append(ord(end)-65)
    root[ord(end)-65] = 0

# 마약수사대가 파악하고 있는 대상을 정수로 변환하여 보관
findList = list(input().split())
findList = findList[1:]
for i in range(len(findList)):
    findList[i] = ord(findList[i]) - 65

# 원산지이며, 마약수사대가 파악하지 못한 대상들 대상으로 dfs 실행
resultSet = set()
def dfs(alphaNum):
    resultSet.add(alphaNum)
    for num in mlist[alphaNum]:
        if num not in findList:
            dfs(num)

for i in range(n):
    if root[i] and i not in findList:
        for each in mlist[i]:
            if each not in findList:
                dfs(each)
             
print(len(resultSet))