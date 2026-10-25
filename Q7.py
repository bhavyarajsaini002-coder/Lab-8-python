s = input().strip()
changes = 0
n = len(s)

for i in range(n//2):
    if s[i] != s[n-1-i]:
        changes += 1
print('Changes needed:',changes)