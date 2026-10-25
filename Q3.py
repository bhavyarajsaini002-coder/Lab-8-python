password = input("Enter password: ")

if len(password) < 8:
    print("weak")
else:
    upper = 0
    lower = 0
    digit = 0
    special = 0

    for char in password:
        if char.isupper():
            upper = 1
        elif char.islower():
            lower = 1
        elif char.isdigit():
            digit = 1
        elif char != '':
            special = 1

        total_types = upper+lower+digit+special

        if total_types == 4:
            print('STRONG')
        elif total_types == 2 or total_types == 3:
            print("MODERATE")
        else:
            print("WEAK")