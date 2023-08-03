n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]
# 경우의 수 2가지
method1 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
            ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
              ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]
method2 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
            ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
              ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
result = float('inf')

for i in range(n-7):
    for j in range(m-7):
        # 8 * 8 체스판 자르기
        # 2개의 경우의 수와 비교하여 최소값으로 갱신
        sliceGraph = [row[j:j+8] for row in graph[i:i+8]]  
        cnt1 = 0
        cnt2 = 0
        for k in range(8):
            for s in range(8):
                if method1[k][s] != sliceGraph[k][s]:
                    cnt1 += 1
                if method2[k][s] != sliceGraph[k][s]:
                    cnt2 += 1

        result = min(cnt1, cnt2, result)

print(result)        