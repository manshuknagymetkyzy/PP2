s = input()
ans = ""
for i in range(len(s)):
    if i % 3 == 0:
        continue
    ans = ans + s[i]
print(ans)
    