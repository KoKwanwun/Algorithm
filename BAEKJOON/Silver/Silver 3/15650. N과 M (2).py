n, m = map(int, input().split())
mlist = []

def back():
    if len(mlist) == m:
        print(" ".join(map(str, mlist)))
        return
    
    for i in range(1, n+1):
        # mlist가 비어있거나 / mlist에 i가 없고 마지막 값보다 i가 클 때
        if (len(mlist) == 0) or (i not in mlist and mlist[-1] < i):
            mlist.append(i)
            back()
            mlist.pop()

back()