W, H = map(int, input().split())
x, y, E = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
code = input()
STATUS = ""
steps = 0

def trans(k):
    global x, y
    xn, yn = x, y
    match k:
        case "N":
            yn += 1
        case "S":
            yn -= 1
        case "E":
            xn += 1
        case "W":
            xn -= 1
    if check == 1:
        if xn < 0 or yn < 0 or xn >= W or yn >= H:
            return "WALL"
        if x1 <= xn <= x2 and y1 <= yn <= y2:
            return "BLOCKED"
    else:
        x, y = xn, yn
        return x, y

for i in range(len(code)):
    result = trans(code[i])
    if E == 0:
        STATUS = "EMPTY"
        break
    check = 1
    if result == "WALL":
        STATUS = "WALL"
        break
    elif result == "BLOCKED":
        STATUS = "BLOCKED"
        break

    check = 0
    trans(code[i])
    E -= 1
    steps += 1

if STATUS == "":
    STATUS = "DONE"
print(STATUS, x, y, E, steps)