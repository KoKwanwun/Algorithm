from collections import deque

n, k = map(int, input().split())

# queue 실패로 deque 사용 (시간 초과)
dq = deque()
for i in range(1, n+1):
    dq.append(i)
result = []

while dq:
    for _ in range(k - 1):              # k-1만큼 앞에 있는 것을 뒤에 붙여주는 작업 반복
        dq.append(dq.popleft())         # k번째는 result에 넣기
    result.append(str(dq.popleft()))    # str은 join을 사용하기 위해

print("<" + ", ".join(result) + ">")