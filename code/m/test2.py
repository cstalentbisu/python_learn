def x(a = []):
    print(id(a))
    a += [5]
    print(id(a))
print(x.__defaults__)
x()
x()
print(x.__defaults__)