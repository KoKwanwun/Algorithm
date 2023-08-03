# 이중 DP를 만든 후
# A[i] == B[j]이라면, 왼쪽 대각선에 있는 DP값 +1
# 그 외는, 위쪽과 왼쪽 값의 MAX값으로 갱신
# 마지막 위치에 있는 값이 LCS의 값

A = [0] + list(input())
B = [0] + list(input())

dp = [[0] * (len(B)) for _ in range(len(A))]

for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(A)-1][len(B)-1])