from itertools import combinations

mlist = list(input().rstrip())
result = set()
stack = []
bracketStack = []

# 괄호의 시작점과 끝점 리스트 저장
for idx, word in enumerate(mlist):
    if word == '(':
        stack.append(idx)
    elif word == ')':
        bracketStack.append((stack.pop(), idx))
        
for i in range(1, len(bracketStack) + 1):
    # 조합으로 제거할 괄호쌍 뽑기
    comb = combinations(bracketStack, i)
    
    for j in comb:
        # 문자열 복사
        tmp = mlist[:]

        for k in j:
            tmp[k[0]] = ""
            tmp[k[1]] = ""
            
        result.add(''.join(tmp))

for each in sorted(list(result)):
    print(each)