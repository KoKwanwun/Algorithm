n, m = map(int, input().split())
mlist = []

def back():
    if len(mlist) == m:
        print(" ".join(map(str, mlist)))
        return
    
    for i in range(1, n+1):
        if len(mlist) == 0 or mlist[-1] <= i:   # 원소가 없거나, 마지막 값이 i보다 크거나 같을 때
            mlist.append(i)
            back()
            mlist.pop()

back()