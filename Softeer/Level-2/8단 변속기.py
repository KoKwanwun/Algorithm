import sys

mlist = list(map(int, input().split()))

if mlist == [1, 2, 3, 4, 5, 6, 7, 8]:
    print("ascending")
elif mlist == [8, 7, 6, 5, 4, 3, 2, 1]:
    print("descending")
else:
    print("mixed")