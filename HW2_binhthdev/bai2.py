d, m, y = map(int, input().split())

def check(d, m, y):
    if d > DoM or d < 1:
        return "INVALID"
    elif d == DoM:
        d = 0
        m += 1
        if m == 13:
            m = 1
            y += 1
    return f"{d + 1:02d}/{m:02d}/{y:04d}"

match m:
    case 1|3|5|7|8|10|12:
        DoM = 31
        print(check(d, m, y))
    case 4|6|9|11:
        DoM = 30
        print(check(d, m, y))
    case 2:
        if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
            DoM = 29
            print(check(d, m, y))
        else:
            DoM = 28
            print(check(d, m, y))