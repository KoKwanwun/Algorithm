from itertools import combinations

# 옷의 종류의 개수를 리스트로 만들어 리턴
def makeList(clothes):
    dict = {}

    for element in clothes:
        clothType = element[1]
        
        tmpValue = 0 if dict.get(clothType) == None else dict.get(clothType)
        tmpValue += 1

        dict[clothType] = tmpValue

    return list(dict.values())

def solution(clothes):
    mlist = makeList(clothes)

    answer = 1
    
    # 수학 계수의 합 이용
    # (x+a)(x+b)(x+c) -> 계수 : 1 + (a+b+c) + (ab+bc+ca) + (abc)
    # x에 1을 넣으면 계수의 합을 구할 수 있음
    # 1은 조합에 포함이 안되므로 리턴 시 -1
    for clothCnt in mlist:
        answer *= (clothCnt + 1)
    
    return answer - 1