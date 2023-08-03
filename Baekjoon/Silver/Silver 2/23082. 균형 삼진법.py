n = int(input())

if n == 0:
    print(0)
else:
    flag = 0
    if n < 0:
        flag = 1
        n *= -1

    result = []
    while n > 0:
        r = n % 3
        if r == 2:
            r = -1
            result.append("T")
        else:
            result.append(str(r))
        n -= r
        n //= 3
        
    if flag == 1:
        for i in range(len(result)):
            if result[i] == "1":
                result[i] = "T"
            elif result[i] == "T":
                result[i] = "1"
        
    print("".join(result[::-1]))