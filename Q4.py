text = input(" Enter the string: ")
ch = input("Enter the character: ")

count = 0
positions =[]

for i in range(len(text)):
    if text[i] == ch:
        count = count + 1
        positions.append(str(i))

print("Count:",count)

if count == 0:
    print("Positions: -1")
else:
    print("Positions:"+" ".join(positions))