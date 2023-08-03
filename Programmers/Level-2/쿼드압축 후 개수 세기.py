def solution(arr):
    answer = [0, 0]
    
    # 재귀 활용
    def back(x, y, n):
        # 첫번째 값 담기
        num = arr[x][y]

        # 주어진 범위를 돌면서 num과 다른것이 나오면 재귀
        for i in range(x, x+n):
            for j in range(y, y+n):
                if arr[i][j] != num:
                    back(x, y, n//2)
                    back(x+n//2, y, n//2)
                    back(x, y+n//2, n//2)
                    back(x+n//2, y+n//2, n//2)
                    return

        # 쿼드트리 완성된다면 개수 더하기
        if num == 1:
            answer[1] += 1
        else:
            answer[0] += 1
    
    back(0, 0, len(arr))
    
    return answer