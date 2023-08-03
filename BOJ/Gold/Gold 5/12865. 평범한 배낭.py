# Knapsack 알고리즘
n, k = map(int, input().split())
mlist = [[0, 0]]
result = [[0 for _ in range(k+1)] for _ in range(n+1)]

for _ in range(n):
    mlist.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = mlist[i][0] 
        value = mlist[i][1]
       
        if j < weight:
            result[i][j] = result[i - 1][j] #weight보다 작으면 위의 값을 그대로 가져온다
        else:
            result[i][j] = max(value + result[i - 1][j - weight], result[i - 1][j])

print(result[n][k])