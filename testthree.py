def f():
    x = [0, -1, 1]
    while True:
        x[0] = x[1] + x[2]
        x[1] = x[2] + x[0]
        x[2] = x[0] + x[1]
        yield x[0]
        yield x[1]
        yield x[2]

b = f()
for i in range(10):
    print(next(b), end=" ")
