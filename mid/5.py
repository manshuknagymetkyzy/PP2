sent = input().split()
lon_w = ""
len_w = 0
for i in sent:
    if len_w < len(i):
        len_w = len(i)
        lon_w = i
print(lon_w)
print(len_w)