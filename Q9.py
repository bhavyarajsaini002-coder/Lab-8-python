s = input()
k = int(input())

ans = ''

for ch in s:
    if ch == ' ':
        ans += ' '
    else:
        pos = ord(ch)-ord('a')
        pos = (pos+k)%26
        ans += chr(pos+ord('a'))

print(ans)