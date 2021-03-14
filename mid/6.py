n = int(input())
array = input().split()
k = int(input())
str_num = str()
for i in array:
    str_num +=i
print(int(str_num[0:k]) * int(str_num[k:n]))