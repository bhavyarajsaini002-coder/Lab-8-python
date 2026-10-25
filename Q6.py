s = input().strip()

if len(s) != 10:
    print("False")
else:
    if (s[:2] == "RJ" and
        s[2:4].isdigit() and
        s[4:6].isupper() and
        s[6:10].isdigit()):
        print("True")
    else:
        print("False")