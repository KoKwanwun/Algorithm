import sys

result = 0

for _ in range(5):
    start, end = map(str, input().split())
    start = int(start.split(":")[0]) * 60 + int(start.split(":")[1])
    end = int(end.split(":")[0]) * 60 + int(end.split(":")[1])
    result += (end - start)

print(result)