n = int(input())
mlist = []

def back():
    if len(mlist) == n:
        print(" ".join(map(str, mlist)))
        return
    
    for i in range(1, n+1):
        if i not in mlist:      # mlist에 i가 존재하지 않을 경우만
            mlist.append(i)
            back()
            mlist.pop()

back()