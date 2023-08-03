from collections import deque
import sys
dq = deque()

for i in range(int(input())):
    line = sys.stdin.readline().split()
    if(line[0] == "push_front"):
        dq.appendleft(line[1])
    elif(line[0] == "push_back"):
        dq.append(line[1])
    elif(line[0] == "pop_front"):
        print(dq.popleft() if(len(dq) != 0) else -1)
    elif(line[0] == "pop_back"):
        print(dq.pop() if(len(dq) != 0) else -1)
    elif(line[0] == "size"):
        print(len(dq))
    elif(line[0] == "empty"):
        print(1 if(len(dq) == 0) else 0)
    elif(line[0] == "front"):
        print(dq[0] if(len(dq) != 0) else -1)
    elif(line[0] == "back"):
        print(dq[-1] if(len(dq) != 0) else -1)