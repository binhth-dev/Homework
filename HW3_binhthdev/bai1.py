username = input()
password = input()
count_upper = 0
count_lower = 0
count_digit = 0
count_sp = 0
index_i = -1
code = 0

if 8 <= len(password) <= 20:
    for i in password:
        index_i += 1
        if index_i >= 2 and password[index_i-2] == password[index_i-1] == password[index_i]:
            code = 1
        if ord(i) in (33, 35, 36, 64):
            count_sp += 1
        elif i.isupper():
            count_upper += 1
        elif i.islower():
            count_lower += 1
        elif i.isdigit():
            count_digit += 1
        else:
            print("INVALID_CHAR")
            exit()
    if count_upper >= 2 and count_lower >= 2 and count_digit >= 2 and count_sp >= 1:
        if code != 1:
            if username.lower() not in password.lower():
                print("STRONG")
            else:
                print("PERSONAL")
        else:
            print("REPEATED")
    else:
        print("WEAK_CLASSES")
        exit()
else:
    print("INVALID_LENGTH")