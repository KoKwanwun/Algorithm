for _ in range(int(input())):
    n = int(input())
    mlist = []
    
    # 예외 : 1이면 1
    if n == 1:
        print(1)
        continue
    
    # 2부터 9까지 한다면 20이 225와 같이 표현됨
    # 9부터 2까지 해야 20이 45로 최소 길이가 됨
    for i in range(9, 1, -1):
        if n % i == 0:
            while True:
                if n % i != 0:
                    break
                mlist.append(i)
                n //= i
        
    # n이 1이 아니라면 26 -> 2 13과 같이 약수에 2자리 이상의 수가 들어감
    if n != 1:
        print(-1)
    else:
        print(len(mlist))