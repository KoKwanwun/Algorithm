import sys

n, k = map(int, sys.stdin.readline().split())

# 한줄로 받아서 정수를 리스트화
mlist = list(map(int,sys.stdin.readline().split()))
    
# 리스트 오름차순 정렬
mlist = sorted(mlist)

print(mlist[k-1])