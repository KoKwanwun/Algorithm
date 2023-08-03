n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

white = 0
blue = 0

def back(x, y, v):
    global white, blue

    # 첫 색깔 지정
    # for문을 돌며 색이 다르면 재귀
    color = graph[x][y]
    for i in range(x, x+v):
        for j in range(y, y+v):
            if color != graph[i][j]:
                back(x, y, v//2)
                back(x, y+v//2, v//2)
                back(x+v//2, y, v//2)
                back(x+v//2, y+v//2, v//2)
                return

    if color == 0:
        white += 1
    else:
        blue += 1
    
back(0, 0, n)
print(white)
print(blue)