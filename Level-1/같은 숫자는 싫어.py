# 원소의 순서를 유지해야했기 때문에 list(set()) 불가 (set은 순서가 없기 때문)
def solution(arr):
    answer = [arr[0]]
    for i in range(1, len(arr)):
        if answer[-1] != arr[i]:
            answer.append(arr[i])
            
    return answer