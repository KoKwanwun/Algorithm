n, m = map(int, input().split())
knowList = set(input().split()[1:])
partyList = []

for _ in range(m):
    partyList.append(set(input().split()[1:]))
    
# 파티의 수만큼 반복 (새롭게 knowList에 추가된다면 다시 확인해야 함)
# 교집합을 활용해서 knowList에 있는 사람이 있다면 해당 파티의 인원을 knowList에 추가
for _ in range(m):
    for party in partyList:
        if party & knowList:
            knowList = knowList.union(party)    

# 과장해서 말할 수 있는 파티 수 구하기
result = 0
for party in partyList:
    if party & knowList:
        continue
    result += 1
    
print(result)