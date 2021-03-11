n, m = map(int, input().split())
anya = set()
borya = set()
for x in range(n):
    anya.add(int(input()))
for y in range(m):
    borya.add(int(input()))
print(len(anya.intersection(borya)))
print(*sorted(anya.intersection(borya)))
print(len(anya.difference(borya)))
print(*sorted(anya.difference(borya)))
print(len(borya.difference(anya)))
print(*sorted(borya.difference(anya)))