def solution(m, n, puddles):
    arr = [[0 for _ in range(m)] for _ in range(n)]
    for puddle in puddles:
        arr[puddle[1]-1][puddle[0]-1] = -1

    for i in range(n):
        for j in range(m):
            if((i == 0 and j == 0) or (arr[i][j] == -1)):
                continue
            elif(i == 0):
                if(arr[i][j-1] == -1):
                    arr[i][j] = -1
                else:
                    arr[i][j] = 1
            elif(j == 0):
                if(arr[i-1][j] == -1):
                    arr[i][j] = -1
                else:
                    arr[i][j] = 1
            else:
                if((arr[i][j-1] == -1) and (arr[i-1][j] == -1)):
                    arr[i][j] = -1
                elif(arr[i][j-1] == -1):
                    arr[i][j] = arr[i-1][j]
                elif(arr[i-1][j] == -1):
                    arr[i][j] = arr[i][j-1]
                else:
                    arr[i][j] = arr[i][j-1] + arr[i-1][j]

    if(arr[n-1][m-1] == -1):
        return 0
    else:    
        return arr[n-1][m-1] % 1000000007

print(solution(2, 2, []), 2)
print(solution(3, 3, []), 6)
print(solution(3, 3, [[2, 2]]), 2)
print(solution(3, 3, [[2, 3]]), 3)
print(solution(3, 3, [[1, 3]]), 5)
print(solution(3, 3, [[1, 3], [3, 1]]), 4)
print(solution(3, 3, [[1, 3], [3, 1], [2, 3]]), 2)
print(solution(3, 3, [[1, 3], [3, 1], [2, 3], [2, 1]]), 1)
print(solution(7, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]), 0) # 이 값이 잘 나오면 테스트1, 테스트9 통과, 위로 가면 안됨
print(solution(4, 4, [[3, 2], [2, 4]]), 7)
print(solution(100, 100, []), 690285631)