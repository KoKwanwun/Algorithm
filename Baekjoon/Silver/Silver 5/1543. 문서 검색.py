a = input()
b = input()
result = 0
idx = 0

while idx < len(a):
    if a[idx:idx+len(b)] == b:
        result += 1
        idx += len(b) - 1
    idx += 1 
    
print(result)