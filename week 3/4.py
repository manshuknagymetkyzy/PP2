a = list(map(int, input().split()))
cnt = 0
for i in a:
    if (i != 0):
        print(i, end = ' ')
    else:
        cnt += 1
print('0 ' * cnt)