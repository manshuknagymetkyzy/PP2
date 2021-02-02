h, m, s = map(int, input().split())
h2, m2, s2 = map(int, input().split())
print((h2*3600 + m2*60 + s2) - (h* 3600 + m*60 + s))