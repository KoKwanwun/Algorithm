def solution(strings, n):
    # 특정 기준으로 정렬 후, 같다면 사전 순으로 정렬
    return sorted(strings, key=lambda x : (x[n], x))