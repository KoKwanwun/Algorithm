# 1*3, 3*2의 곱이라면, 결과 행(1) 결과 열(2) 중간 개수(3)
def solution(arr1, arr2):
    result = []                         # 결과 리스트

    for i in range(len(arr1)):          # 결과 행 개수만큼
        mlist = []                      # 결과 행 임시 리스트
        
        for j in range(len(arr2[0])):   # 결과 열 개수만큼
            element = 0                 # 원소 값

            for k in range(len(arr2)):  # 중간 개수 만큼
                element += arr1[i][k] * arr2[k][j]

            mlist.append(element)       # 계산 후 임시 리스트에 넣기

        result.append(mlist)            # 행 완성시 결과 리스트에 넣기
    
    return result