import sys

a, b = map(int, input().split())

if a < b:
    print("B")
elif a > b:
    print("A")
else:
    print("same")