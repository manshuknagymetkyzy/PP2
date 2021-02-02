k = int(input())
h = k // 3600
m = (k - 3600*h) // 60
ans = "It is {} hours {} minutes."
print(ans.format(h, m))