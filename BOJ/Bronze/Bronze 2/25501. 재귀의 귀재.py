import sys
sys.setrecursionlimit(1000000)

def recursion(s, l, r):
    global n;
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        n += 1
        return recursion(s, l+1, r-1)

for _ in range(int(input())):
    strs = input()
    n = 1
    print(recursion(strs, 0, len(strs)-1), n)