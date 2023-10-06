# 문자열을 붙여 반지처럼 보이도록 변환
s = input()
result = 0

for _ in range(int(input())):
    tmp = input()
    tmp += tmp
    
    if s in tmp:
        result += 1
        
print(result)