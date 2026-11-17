n = int(input())

tong_tien = n * 1500
if n > 50:
    n -= 50
    tong_tien += n * (2000 - 1500)
    if n > (100 - 50):
        n -= 100 - 50
        tong_tien += n * (3000 - 2000)

print(f"{tong_tien * 1.05:.0f}")