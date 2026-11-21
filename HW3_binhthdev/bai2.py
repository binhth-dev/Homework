B, L, n= map(int,input().split())
result = []
for _ in range(n):
    request = int(input())
    if request <= 1000:
        fee = 10
    else:
        fee = 20
    if request > 0 and request % 50 == 0:
        if request <= 5000:
            if request <= L:
                if (B - request - fee) >= 0:
                    result.append("OK")
                    B = B - request - fee
                    L -= request
                else:
                    result.append("INSUFFICIENT")
            else:
                result.append("DAILY_LIMIT")
        else:
            result.append("LIMIT")
    else:
        result.append("INVALID")
result.append(f"{B} {L}")
print("\n".join(result))