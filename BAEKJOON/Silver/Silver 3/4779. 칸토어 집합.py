def recursion(n, i, j):
    if n < 1:
        return
    
    # 3등분
    cnt = (j - i) // 3
    # 왼쪽
    recursion(n-1, i, i + cnt)
    # 가운데
    for k in range(i + cnt, i + cnt * 2):
        answer[k] = ' '
    # 오른쪽
    recursion(n-1, i + cnt * 2, i + cnt * 3)

# 파이썬 입력이 끝날때까지 EOF
while True:
    try:
        n = int(input())
        answer = ["-"] * (3 ** n)
        recursion(n, 0, 3 ** n)
        print(''.join(answer))
    except:
        break