bai_tap = input("Bài số: ")
if bai_tap == "1":
    n = input()
    n = int(n)
    if 1000 > n > 99:
        a = n % 10
        b = n % 100 - a
        c = n - b - a
        n_rev = a * 100 + b + c / 100
        print(int(n_rev))
    else:
        print("Không xử lí")
elif bai_tap == "2":
    a, b = input().split()
    a = int(a)
    b = int(b)
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(a, b)
elif bai_tap == "3":
    while True:
        try:
            n = input()
            n = int(n)
            if n & n - 1 == 0:
                print("Đây là số chẵn")
            else:
                print("Đây là số lẻ")
        except ValueError:
            print("Chỉ nhập số nguyên")
else:
    print("Chưa có bài này")