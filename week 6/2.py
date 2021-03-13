def sum(n):
  total = 0
  for i in n:
    total += i
  return total
print(sum(list(map(int, input().split()))))