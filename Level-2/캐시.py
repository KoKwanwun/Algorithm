from collections import deque

# LRU : Head에 값을 차례대로 넣고, 기존 캐시에 값이 있다면 Head로 땡겨주고 hit, 값이 없다면 miss

def solution(cacheSize, cities):
    cities = map(lambda x: x.lower(), cities)   # 대소문자 구분 해결
    cache = deque()
    result = 0
    
    for i in range(len(cities)):
        if cities[i] in cache:                  # 캐시에 있다면 hit, 앞으로 땡겨주기
            result += 1
            cache.appendleft(cities[i])
            cache.remove(cities[i])
        elif len(cache) >= cacheSize:           # 캐시 사이즈가 넘는다면, head에 넣고 tail값 없애기
            result += 5
            cache.pop()
            cache.appendleft(cities[i])
        else:                                   # 그 외는 캐시 사이즈 안이기 때문에 head에 넣기
            result += 5
            cache.appendleft(cities[i])

    return result