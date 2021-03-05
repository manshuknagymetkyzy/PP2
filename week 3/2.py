a = list(map(int, input().split()))
min = 1001
for i in a:
    if(i < min and i > 0):
        min = i
print(min)