mlist = list(input())

# 13을 알파벳(아스키코드)에 더해서 암호화
for i in range(len(mlist)):
    if(ord(mlist[i]) >= 65 and ord(mlist[i]) <= 90):
        mlist[i] = chr((ord(mlist[i]) - 52) % 26 + 65)
    elif(ord(mlist[i]) >= 97 and ord(mlist[i]) <= 122):
        mlist[i] = chr((ord(mlist[i]) - 84) % 26 + 97)
    else:
        continue

print(''.join(mlist))