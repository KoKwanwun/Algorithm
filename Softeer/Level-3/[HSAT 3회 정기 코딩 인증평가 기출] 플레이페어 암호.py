import sys

message = list(input())
keys = list(set(input()))   # 중복 제거
alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", 
"P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# 키 중 없는 알파벳을 순서대로 넣기
for alphabet in alphabets:
    if alphabet not in keys:
        keys.append(alphabet)

# 5 * 5 테이블로 변환
table = []
for i in range(0, len(keys), 5):
    table.append(list(keys[i:i+5]))

# dictionary를 활용하여 각 알파벳별 위치 저장
keys_idx = dict()
for i in range(5):
    for j in range(5):
        keys_idx[table[i][j]] = [i, j]

# 메세지 규칙에 의해 재 정의
new_message = []
idx = 0
while True:
    if idx >= (len(message) - 1):
        break

    if message[idx] == message[idx+1]:
        new_message.append(message[idx])
        if message[idx] == "X":
            new_message.append("Q")
        else:
            new_message.append("X")
        idx += 1
    else:
        new_message.append(message[idx])
        new_message.append(message[idx+1])
        idx += 2

if idx == (len(message) - 1):
    new_message.append(message[-1])

if len(new_message) % 2:
    new_message.append("X")

# 암호화
result = ""
for i in range(0, len(new_message), 2):
    xRow = keys_idx[new_message[i]][0]
    xCol = keys_idx[new_message[i]][1]
    yRow = keys_idx[new_message[i+1]][0]
    yCol = keys_idx[new_message[i+1]][1]

    # 행이 같을 경우
    if xRow == yRow:
        result += table[xRow][(xCol + 1) % 5]
        result += table[yRow][(yCol + 1) % 5]
    # 열이 같을 경우
    elif xCol == yCol:
        result += table[(xRow + 1) % 5][xCol]
        result += table[(yRow + 1) % 5][yCol]
    # 외의 경우
    else:
        result += table[xRow][yCol]
        result += table[yRow][xCol]

print(result)