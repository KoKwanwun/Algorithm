n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

result = [0, 0, 0]

def back(x, y, v):
    global result
    num = graph[x][y]
    
    # 초기값과 다를경우, 9구간으로 나눠야하기 때문에 9번 재귀하도록 설정
    for i in range(x, x+v):
        for j in range(y, y+v):
            if num != graph[i][j]:
                back(x, y, v//3)
                back(x, y+v//3, v//3)
                back(x, y+(2*v//3), v//3)
                back(x+v//3, y, v//3)
                back(x+(2*v//3), y, v//3)
                back(x+v//3, y+v//3, v//3)
                back(x+v//3, y+(2*v//3), v//3)
                back(x+(2*v//3), y+v//3, v//3)
                back(x+(2*v//3), y+(2*v//3), v//3)
                return

    if num == -1:
        result[0] += 1
    elif num == 0:
        result[1] += 1
    else:
        result[2] += 1

back(0, 0, n)
for i in range(3):
    print(result[i])