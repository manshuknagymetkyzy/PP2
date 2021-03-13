def max(x, y, z):
    if(x > y):
        if(x > z):
            return x
        else:
            return z
    else:
        if(y > z):
            return y
        else:
            return z
x, y, z = map(int, input().split())
print max(x, y, z)