s = input()

if len(s) == 0:
    print(" ")
else:
    count = 1
    maximum = 1
    character = s[0]

for i in range(1,len(s)):
    if s[i] == s[i-1]:
        count += 1 
    else:
        count = 1

    if count > maximum:
        maximum  = count
        character = s[i]

print(character,maximum)