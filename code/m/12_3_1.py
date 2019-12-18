def fn(n):
    if n == 1:
        return 1
    else:
        return n*fn(n-1)

print(fn(900))