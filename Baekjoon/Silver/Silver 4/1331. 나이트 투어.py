graph = [[0 for _ in range(6)] for _ in range(6)]
mdict = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5}
flag = 0

location = input()
x = mdict[location[0]]
y = int(location[1]) - 1
startx = x
starty = y
graph[x][y] = 1

for _ in range(35):
    location = input()
    a = mdict[location[0]]
    b = int(location[1]) - 1
    
    # 이미 방문한 경우
    if graph[a][b] == 1:
        flag = 1
    # 나이트로 움직일 수 있는 경우
    elif (abs(x - a) == 1 and abs(y - b) == 2) or (abs(x - a) == 2 and abs(y - b) == 1):
        graph[a][b] = 1
        x = a
        y = b
    # 그 외의 경우 (ex. 나이트로 이동할 수 없는 경우)
    else:
        flag = 1

if flag == 0:
    # 마지막 방문한 위치에서 시작점으로 돌아올 수 있을 경우에만
    if (abs(startx - a) == 1 and abs(starty - b) == 2) or (abs(startx - a) == 2 and abs(starty - b) == 1):
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")