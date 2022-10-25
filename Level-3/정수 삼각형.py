def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if(j == 0):
                maxValue = triangle[i-1][0]
            elif(j == (len(triangle[i])-1)):
                maxValue = triangle[i-1][-1]
            else:
                maxValue = max(triangle[i-1][j-1], triangle[i-1][j])

            triangle[i][j] += maxValue

    return max(triangle[-1])