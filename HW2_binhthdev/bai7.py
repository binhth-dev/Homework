n = int(input())
step = 0
max = n

while n > 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
        if max < n:
            max = n
    step += 1

print(f"{step} {max}")