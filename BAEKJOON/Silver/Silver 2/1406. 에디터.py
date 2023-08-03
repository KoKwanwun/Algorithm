import sys

# 2개의 Stack 사용 (append, pop을 O(1)로 보장 가능)
st1 = list(sys.stdin.readline().rstrip())
st2 = []

for _ in range(int(sys.stdin.readline())):
	command = list(sys.stdin.readline().split())
	
    # 1에서 하나 빼서 2에 넣기
	if command[0] == 'L':
		if st1:
			st2.append(st1.pop())

    # 2에서 하나 빼서 1에 넣기    
	elif command[0] == 'D':
		if st2:
			st1.append(st2.pop())

    # 1에서 하나 빼기
	elif command[0] == 'B':
		if st1:
			st1.pop()
            
    # 1에 추가
	else:
		st1.append(command[1])
        
st1.extend(reversed(st2))
print(''.join(st1))