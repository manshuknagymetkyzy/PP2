n = int(input())
a = set(map(int, input().split()))
for i in range(len(a)):
    print(i + 1, a[i])