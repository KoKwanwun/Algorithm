from itertools import permutations
def cal(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2

def solution(expression):
    result = 0
    
    # 정수만 분리
    nums = expression
    nums = nums.replace('+', ' ')
    nums = nums.replace('-', ' ')
    nums = nums.replace('*', ' ')
    nums = list(map(int, nums.split(' ')))
    
    # 연산자만 분리
    operands = []
    for each in expression:
        if not each.isdecimal():
            operands.append(each)
    
    # 연산자 우선순위별로 for문
    for each in permutations(['*', '+', '-'], 3):
        copy_nums = nums
        copy_operands = operands
        
        # 각 연산자 수행
        for formula in each:
            stack_nums = []
            stack_operands = []
            stack_nums.append(copy_nums[0])
            
            # stack 활용 수행할 연산자가 나오면 수행
            for i in range(len(copy_operands)):
                stack_nums.append(copy_nums[i+1])
                stack_operands.append(copy_operands[i])
                
                if formula == stack_operands[-1]:
                    num1 = stack_nums.pop()
                    num2 = stack_nums.pop()
                    op = stack_operands.pop()
                    # 순서대로 하기 위해 num2, num1 순서대로 함수에 넣기
                    stack_nums.append(cal(num2, num1, op))
        
            copy_nums = stack_nums
            copy_operands = stack_operands
            
        result = max(result, abs(copy_nums[0]))
        
    return result