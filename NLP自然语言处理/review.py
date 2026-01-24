
def fun():
    for value in [1, 2, 2]:
        yield value

a = fun()
print(a)
print(next(a))
