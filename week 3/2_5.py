n = int(input())
m = {}
for i in range(n):
    x, y = input().split()
    m[x] = y
    m[y] = x
s = input()
print(m[s])