temp = 0
print(type(temp))

value = (type(temp) == int)
print(value)

class A:
    pass

print(isinstance(A(), A))