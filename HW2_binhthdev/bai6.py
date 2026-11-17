n = int(input())
i = 2
list1 = []
while i * i <= n:
    count = 0
    while n % i == 0:
        n //= i
        count += 1
    if count > 0:
        list1.append(f"{i}^{count}")
    i += 1
if n > 1:
    list1.append(f"{n}^1")
print(" ".join(list1))