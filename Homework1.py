import math

k = input("Bài số: ")
if k == "1":
    n = input()
    n = int(n)
    print(n * 2)
elif k == "2":
    a = float(input())
    b = float(input())
    s = 3.14 * (a/2)**2
    print(f"{a * b - s: .2f}") 
elif k == "3":
    c = input()
    if c.isupper():
        print(c.lower())
    elif c. islower():
        print(c.upper())
elif k == "4":
    c = input()
    if c.isalpha():
        print(f"{{{c}}} là kí tu alphabet")
    elif c.isdigit():
        print(f"{{{c}}} không phải là kí tự alphabet")
elif k == "5":
    A = input()
    if A == "A":
        print("z")
    else:
        a = ord(A) - 1
        print(chr(a).lower())
elif k == "6":
    a, b, c = map(float, input().split())
    if a + b > c and abs(a - b) < c:
        p = (a + b + c) / 2
        print(f"{math.sqrt(p * (p - a) * (p - b) * (p - c)): .1f}")
    else:
        print("Khong phai 3 canh cua tam giac")
elif k == "7":
    n = input()
    print(n[5], n[9])
elif k == "8":
    name = input("Ten chu ho: ")
    so_dien_1 = float(input("Chi so thang truoc: "))
    so_dien_2 = float(input("Chi so thang nay: "))
    chenh_lech = so_dien_2 - so_dien_1
    method = input("Giải theo kiểu: ")
    if method == "1":
        if chenh_lech > 0:
            tien_dien = chenh_lech * 1984
            chenh_lech = chenh_lech - 50
            if chenh_lech > 0:
                tien_dien = chenh_lech * (2050 - 1984) + tien_dien
                chenh_lech = chenh_lech - 50
                if chenh_lech > 0:
                    tien_dien = chenh_lech * (2380 - 2050) + tien_dien
                    chenh_lech = chenh_lech - 100
                    if chenh_lech > 0:
                        tien_dien = chenh_lech * (2998 - 2380) + tien_dien
                        chenh_lech = chenh_lech - 100
                        if chenh_lech > 0:
                            tien_dien = chenh_lech * (3350 - 2998) + tien_dien
                            chenh_lech = chenh_lech - 100
                            if chenh_lech > 0:
                                tien_dien = chenh_lech * (3460 - 3350) + tien_dien
    if method == "2":
        bacs = [(50, 1984), (50, 2050), (100, 2380), (100, 2998), (100, 3350), (float('inf'), 3460)]
        kwh = so_dien_2 - so_dien_1
        tien = 0
        for so_kwh, gia in bacs:
            if kwh <= 0: 
                break
            dung = min(kwh, so_kwh)
            tien += dung * gia
            kwh -= dung
        tien_dien = tien
    print(f"Ho va ten: {name}")
    print(f"Tien phai tra la: {tien_dien * 1.08: .0f}")
else:
    print("Chưa có bài này")