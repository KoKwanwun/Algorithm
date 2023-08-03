n, m = map(int, input().split())
mlist = []

# 예시
# n=4, m=2
# mlist : [1] -> [1,2] -> [1] -> [1,3] -> [1] -> [1,4] -> ...
def back():
    if len(mlist) == m:
        print(" ".join(map(str, mlist)))
        return
    
    for i in range(1, n+1):
        if i not in mlist:      # 1~n 중 mlist에 없으면 넣기
            mlist.append(i)
            back()
            mlist.pop()
            
back()