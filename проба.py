a = 5
c = a
print(a, id(a), c, id(c))

a = 8
print(a, id(a), c, id(c))

x = [1,2,3,4]
y = x
print(x, id(x), y, id(y))

x.append(10)
print(x, id(x), y, id(y))