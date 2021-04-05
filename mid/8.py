a = list(map(str, input().split()))
a.sort()
d = {}
for x in a:
    if x not in d:
        d[x] = 1
    else:
        d[x] += 1
for x, y in d.items():
    print(x, y)