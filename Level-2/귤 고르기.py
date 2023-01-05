from collections import Counter

def solution(k, tangerine):
    # 귤이 많은 크기의 개수를 내림차순하여 sumList에 넣기
    sumList = sorted(Counter(tangerine).values(), reverse = True)
    sumNum = 0
    
    # sumList에서 하나씩 꺼내서 sumNum에 더한 후, k보다 크거나 같아지면 인덱스 +1 리턴
    """
    예시
    k = 6, [1,3,2,5,4,5,2,3] -> sumList = [2,2,2,1,1]
    2 + 2 + 2 = 6, k와 동일하기 때문에 3리턴(인덱스는 2이기 때문에 +1 하여 리턴)
    """
    for i in range(len(sumList)):
        sumNum += sumList[i]
        if(sumNum >= k):
            return i + 1