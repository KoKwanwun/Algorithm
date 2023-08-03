n = int(input())
n_list = sorted(list(map(int, input().split())))
m = int(input())
targets = list(map(int, input().split()))

cnt = {}
for each in n_list:
    if each in cnt:
        cnt[each] += 1
    else:
        cnt[each] = 1

def binarySearch(n_list, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2
    if n_list[mid] == target:
        return cnt.get(target)
    elif n_list[mid] < target:
        return binarySearch(n_list, target, mid+1, end)
    else:
        return binarySearch(n_list, target, start, mid-1)

for target in targets:
    print(binarySearch(n_list, target, 0, len(n_list)-1), end = ' ')