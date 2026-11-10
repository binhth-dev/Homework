import math
from decimal import Decimal

k = input("Bài số: ")

if k == "1":
    a, b = map(float, input().split())
    print(f"{a * b}\n{2 * (a + b)}")
elif k == "2":
    r = float(input())
    print(f"{3.14 * r**2}\n{2 * 3.14 * r}")
elif k == "3":
    m = input("Giải theo cách: ")
    if m == "1":
        def is_right_triangle(a, b, c):
            return (math.isclose(a**2 + b**2, c**2) or
                    math.isclose(a**2 + c**2, b**2) or
                    math.isclose(b**2 + c**2, a**2))

        a, b, c = map(float, input().split())

        if a + b <= c or a + c <= b or b + c <= a:
            print("Khong la ba canh cua mot tam giac")
        else:
            if a == b:
                if a == c:
                    print("Đây là tam giác đều")
                else:
                    if is_right_triangle(a, b, c):
                        print("Đây là tam giác vuông cân (tại C)")
                    else:
                        print("Đây là tam giác cân (tại C)")
            elif a == c:
                if is_right_triangle(a, b, c):
                    print("Đây là tam giác vuông cân (tại B)")
                else:
                    print("Đây là tam giác cân (tại B)")
            elif b == c:
                if is_right_triangle(a, b, c):
                    print("Đây là tam giác vuông cân (tại A)")
                else:
                    print("Đây là tam giác cân (tại A)")
            elif is_right_triangle(a, b, c):
                print("Đây là tam giác vuông")
            else:
                print("Đây là tam giác thường")

            t = a + b + c
            p = t/2
            s = math.sqrt(p * (p - a) * (p - b) * (p - c))
            print(f"{t:.2f}\n{s:.2f}")

    elif m == "2":

        def is_right_triangle(a, b, c):
            return (math.isclose(a**2 + b**2, c**2))
        
        a, b, c = sorted(map(float, input().split()))

        if a + b <= c or a + c <= b or b + c <= a:
            print("Khong la ba canh cua mot tam giac")
        else:
            if a == c:
                print("Đây là tam giác đều")
            else:
                if a == b or b == c:
                    if is_right_triangle(a, b, c):
                        print("Đây là tam giác vuông cân")
                    else:
                        print("Đây là tam giác cân")
                elif is_right_triangle(a, b, c):
                    print("Đây là tam giác vuông")
                else:
                    print("Đây là tam giác thường")

            cv = a + b + c
            p = cv / 2
            s = math.sqrt(p * (p - a) * (p - b) * (p - c))
            print(f"{cv}\n{s}")
    else:
        print("Chưa có cách giải này")
elif k == "4":
    a, b = map(float, input().split())
    print(b / a)
elif k == "5":
    a, b, c = map(float, input().split())
    delta = b**2 - 4 * a * c
    delta_2 = math.sqrt(delta)
    if delta > 0:
        print(f"{(-b - delta_2) / (2 * a):.2f}\n{(-b + delta_2) / (2 * a):.2f}")
    elif delta == 0:
        print(f"{-b / (2 * a):.2f}")
    else:
        print("Phương trình vô nghiệm")
elif k == "6":
    a, b, c, d = map(float, input().split())
    print(max(a, b, c, d))
elif k == "7":
    a, b, c, d = map(float, input().split())
    print(min(a, b, c, d))
elif k == "8":
    m = input("Giải theo cách: ")
    if m == "1":
        a, b, c, d, m, n = map(float, input().split())
        if a * d == b * c:
            if a == 0:
                if b == 0:
                    if m == 0:
                        if c == 0:
                            if d == 0:
                                if n == 0:
                                    print("Hệ phương trình có vô số nghiệm")
                                else:
                                    print("Hệ phương trình vô nghiệm")
                            else:
                                print(f"x vô số nghiệm\ny = {n / d:.2f}")
                        elif d == 0:
                            print(f"x = {n/c:.2f}\ny vô số nghiệm")
                        else:
                            print("Hệ phương trình có vô số nghiệm")
                    else:
                        print("Hệ phương trình vô nghiệm")
                else:
                    if d == 0:
                        if n == 0:
                            print(f"x vô số nghiệm\ny = {m/b:.2f}")
                        else:
                            print("Hệ phương trình vô nghiệm")
                    else:
                        if m == n == 0:
                            print("Hệ phương trình có vô số nghiệm")
                        elif b * n == d * m and m != 0 and n != 0:
                            print(f"x vô số nghiệm\ny = {m/b:.2f}")
                        else:
                            print("Hệ phương trình vô nghiệm")
            elif b == 0:
                if m == 0:
                    if c == 0:
                        if d == 0:
                            if n == 0:
                                print("Hệ phương trình có vô số nghiệm")
                            else:
                                print("Hệ phương trình vô nghiệm")
                        else:
                            print(f"x vô số nghiệm\ny = {n / d:.2f}")
                    elif d == 0:
                        if n == 0:
                            print(f"x = 0\ny vô số nghiệm")
                        else:
                            print("Hệ phương trình vô nghiệm")
                    else:
                        print("Hệ phương trình vô nghiệm")
                elif c == 0:
                    if n == 0:
                        print(f"x = {m / a:.2f}\ny vô số nghiệm")
                    else:
                        print("Hệ phương trình vô nghiệm")
                else:
                    if m == n == 0:
                        print("Hệ phương trình có vô số nghiệm")
                    elif a * n == c * m and m != 0 and n != 0:
                        print(f"x = {m / a:.2f}\ny vô số nghiệm")
                    else:
                        print("Hệ phương trình vô nghiệm")
            elif c == 0:
                if d == 0:
                    if n == 0:
                        print("Hệ phương trình có vô số nghiệm")
                    else:
                        print("Hệ phương trình vô nghiệm")
                else:
                    if m == n == 0:
                        print("Hệ phương trình có vô số nghiệm")
                    elif b * n == d * m and m != 0 and n != 0:
                        print(f"x vô số nghiệm\ny = {n/d:.2f}")
                    else:
                        print("Hệ phương trình vô nghiệm")
            elif a * n == c * m and b * n == d * m:
                print("Hệ phương trình có vô số nghiệm")
            else:
                print("Hệ phương trình vô nghiệm")
        else:
            print(f"x = {(m*d-b*n)/(a*d-b*c):.2f}\ny = {(a*n-c*m)/(a*d-b*c):.2f}")
    elif m == "2":
        a, b, c, d, m, n = map(float,input().split())
        D = a * d - b * c
        Dx = d * m - b * n
        Dy = a * n - c * m
        approximate = 1e-9
        if abs(D) > approximate:
            print(f"x = {Dx / D}, y = {Dy / D}")
        elif abs(Dx) <= approximate and abs(Dy) <= approximate:
            print("He co vo so nghiem")
        else:
            print("He vo nghiem")
elif k == "9":
    a = input()
    a = int(a)
    print(f"{a // 3600} giờ, {a // 60 % 60} phút, {a % 60} giây")
elif k == "10":
    a, b, c = map(float(input().split))
    d, e = map(float(input().split))
    distance = math.sqrt((d - a)**2 + (e - b)**2)
    if distance == c:
        print("Điểm A thuộc đường tròn")
    else:
        print("Điểm A không thuộc đường tròn")
elif k == "11":
    x, y = map(Decimal,input().split())
    print(f"{x**y:.2f}")
else:
    print("Chưa có bài này")