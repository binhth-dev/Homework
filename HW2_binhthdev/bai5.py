n = int(input())
if n == 0:
    print("0 0 0")

count = 0
total = 0
reverse = 0

while n > 0:
    char = n % 10
    if char in (2, 3, 5, 7):
        count += 1
        total += char
    reverse = reverse * 10 + char
    n //= 10

print(f"{count} {total} {reverse}")