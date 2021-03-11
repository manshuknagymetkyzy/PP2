n = list(map(int, input().split()))
k = int(input()) % len(n)
if(k > 0):
    print(*n[-k:], end = " ")
    print(*n[:-k])
else:
    k = abs(k)
    print(*n[k:], end = " ")
    print(*n[:k])