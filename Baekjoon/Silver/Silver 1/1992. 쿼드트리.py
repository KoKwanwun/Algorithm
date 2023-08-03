n = int(input())
graph = []
# 붙어서 데이터가 주어지므로, split() 빼기
for _ in range(n):
    graph.append(list(map(int, input())))

result = ""

def back(x, y, v):
    global result
    num = graph[x][y]

    # 같지 않은 것이 나온다면, 괄호 씌우고 재귀
    for i in range(x, x+v):
        for j in range(y, y+v):
            if num != graph[i][j]:
                result += "("
                back(x, y, v//2)
                back(x, y+v//2, v//2)
                back(x+v//2, y, v//2)
                back(x+v//2, y+v//2, v//2)
                result += ")"
                return

    if num == 1:
        result += "1"
    else:
        result += "0"

back(0, 0, n)
print(result)