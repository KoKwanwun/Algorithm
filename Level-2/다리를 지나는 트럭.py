# 별도의 시간 변수를 두지 않고, 다리 위에 트럭이나 0 변수를 넣어 계산
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
    # 다리 위 무게 합 변수
    sumWeight = 0
    
    while bridge:
        answer += 1
        sumWeight -= bridge.pop(0)
        
        if truck_weights:
            if sumWeight + truck_weights[0] <= weight:            
                t = truck_weights.pop(0)
                sumWeight += t
                bridge.append(t)
            else:
                bridge.append(0)
                 
    return answer