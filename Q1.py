s = "Hello JKLU! 302026"

vowels = 0
consonants = 0
digits = 0
spaces = 0
others = 0

for ch in s:
    if ch.lower()in"aeiou":
        vowels += 1 
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        others += 1
print("vowels:",vowels)
print("consonants:",consonants)
print("digits:",digits)
print("spaces:",spaces)
print("others:",others)