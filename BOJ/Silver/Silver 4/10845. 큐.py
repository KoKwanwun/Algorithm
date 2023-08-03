import sys

n = int(sys.stdin.readline())
mlist = []

for _ in range(n):
    s = sys.stdin.readline()
    # push일 경우 정수 리스트에 추가
    if(s[0:4] == "push"):
        mlist.append(int(s[5:]))
    # pop일 경우 첫번째 원소 빼고 출력(비어있으면 -1 출력)
    elif(s[0:3] == "pop"):
        if(len(mlist) == 0):
            print(-1)
        else:
            print(mlist.pop(0))
    # size일 경우 리스트 크기 출력
    elif(s[0:4] == "size"):
        print(len(mlist))
    # empty일 경우 비어있으면 1, 아니면 0 출력
    elif(s[0:5] == "empty"):
        print(1 if len(mlist) == 0 else 0)
    # front일 경우 비어있으면 -1, 아니면 첫번째 원소 출력
    elif(s[0:5] == "front"):
        if(len(mlist) == 0):
            print(-1)
        else:
            print(mlist[0])
    # back일 경우 비어있으면 -1, 아니면 마지막 원소 출력
    elif(s[0:4] == "back"):
        if(len(mlist) == 0):
            print(-1)
        else:
            print(mlist[-1])