mlist = [0] * 10000001
result = []

n = int(input())
for num in list(map(int, input().split())):
    if num >= 0:
        mlist[num] += 1
    else:
        mlist[abs(num)] += 2

m = int(input())
for num in list(map(int, input().split())):
    if num >= 0:
        if mlist[num] == 1 or mlist[num] == 3:
            result.append('1')
        else:
            result.append('0')
    else:
        if mlist[abs(num)] == 2 or mlist[abs(num)] == 3:
            result.append('1')
        else:
            result.append('0')

print(' '.join(result))