import sys
input = sys.stdin.readline

mlist = input().rstrip()
resultList = []
flag = 0
tmp = ""

for each in mlist:
    # &, |은 한번 건너뛰기
    if flag:
        flag = 0
        continue
    
    if each in ('<', '>', '&', '|', '(', ')'):
        # 이전까지의 문자열 리시트에 추가
        if tmp != "":
            resultList.append(tmp)
            
        # &와 |는 연속으로 2개가 나오므로 따로 처리
        if each == '&':
            resultList.append('&&')
            flag = 1
        elif each == '|':
            resultList.append('||')
            flag = 1
        else:
            resultList.append(each)
            
        tmp = ""
    # 공백은 없애기
    elif each == ' ':
        if tmp == "":
            continue
        else:
            resultList.append(tmp)
            tmp = ""
    else:
        tmp += each
if tmp != "":
    resultList.append(tmp)
        
print(' '.join(resultList))

"""
다른 풀이
text = input()
text = text.replace('<', ' < ').replace('>',' > ').replace('&&', ' && ').replace('||', ' || ').replace('(',' ( ').replace(')', ' ) ')
print(" ".join(list(text.split())))
"""