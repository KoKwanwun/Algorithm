# 짝수일 때는 마지막 자리가 0이기 때문에 +1 값이 정답
# 홀수일 때
"""
input data를 2진수 변환했을때 가장 먼저 나오는 0의 자리를 1로 나머지는 0으로
이 숫자를 /2 한 값을 빼주시면 됩니다.
ex) 5 -> 101 -> 가장 먼저 나오는 0을 탐색(2의 1승자리) -> 101 + 1 -> 110 ->output data : 6
ex) 3 -> 11 -> 가장 먼저 나오는 0을 탐색(2의 2승자리) -> 11 + 10 -> 101 ->output data : 5
"""
def solution(numbers):
    answer = []
    
    for num in numbers:
        if num % 2:
            numBit = bin(num)[2:][::-1]
            if '0' in numBit:
                num2 = pow(2, numBit.index('0'))
                answer.append(num + num2 - (num2 // 2))
            else:
                num2 = pow(2, len(numBit))
                print(num2)
                answer.append(num + (num2 // 2))
        else:
            answer.append(num + 1)
        
        numBit = bin(num)[2:]
        
    
    return answer