def mult2(x, y):
    print(f"{x} is being multiplied by {y}")
    return x * y


print(mult2(2, 7))

a = 12
print(mult2(a, 6))

b = 10
print(mult2(a, b))

# ---------------------------------------------


def foo(x):
    x[2] = 99


a = [1, 2, 3, 4]

foo(a)
print(a[2])
print(a)

# -----------------------------------------------


def hello(x):
    print(x)  # hello
    x = x.upper()
    print(x)  # HELLO


a = "hello"
hello(a)

print(a)  # hello

# -----------------------------------------------

def centered_average(a):
    print(a)
    a.sort()
    print(a)

    middle = a[1:-1]
    print(middle)

    total = 0
    for v in middle:
        total += v

    return total // len(middle)
print(centered_average([1, 1, 5, 5, 10, 8, 7]))

# -------------------------------------------------

def centered_average2(a):
    a.remove(min(a))
    a.remove(max(a))

    total = 0
    for v in a:
        total += v

    return total // len(a)
 
print(centered_average2([1, 1, 5, 5, 10, 8, 7]))

# ------------------------------------------------

def centered_average3(a):
    mn = min(a)
    mx = max(a)

    total = 0
    for v in a:
        total += v

    total -= mn
    total -= mx
    return total // (len(a) -2)
 
print(centered_average3([1, 1, 5, 5, 10, 8, 7]))
