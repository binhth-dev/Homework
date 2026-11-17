a, b = map(int, input().split())
initdigit = []

def compare(p1, p2):
    if p1[1] == p2[1]:
        return p1
    elif p1[1] > p2[1]:
        return p1
    else:
        return p2

for i in range(a, b + 1):
    count = 1
    for v in range(2, i + 1):
        if i % v == 0:
            count += 1
    list1 = [i, count] 
    initdigit.append(list1)

Max = initdigit[0]
for m in initdigit[1:]:
    Max = compare(Max, m)

print(*Max)