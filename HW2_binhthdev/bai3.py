l1, r1, l2, r2 = map(int, input().split())

if r1 - l2 < 0:
    print("NONE")
else:
    print(f"{l2} {r1} {r1 - l2 + 1}")