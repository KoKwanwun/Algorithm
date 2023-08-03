n, m = map(int, input().split())
mlist = []

def back():
    if len(mlist) == m:
        print(" ".join(map(str, mlist)))
        return
    
    # 모든 원소를 중복하여 백트래킹
    for i in range(1, n+1):
        mlist.append(i)
        back()
        mlist.pop()

back()