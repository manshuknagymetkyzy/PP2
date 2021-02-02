d = int(input())
h = d // 30
m = (d % 30) * 2
ans = "It is {} hours {} minutes."
print(ans.format(h, m))