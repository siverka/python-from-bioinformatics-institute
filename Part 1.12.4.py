def s_triangle():
    a = float(input("a "))
    b = float(input("b "))
    c = float(input("c "))
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def s_rectangle():
    x = float(input("x "))
    y = float(input("y "))
    return x * y


def s_circle():
    r = float(input("r "))
    return 3.14 * (r ** 2)


figures = {"треугольник": s_triangle, "прямоугольник": s_rectangle, "круг": s_circle}

fig = input("figure ")

print(figures[fig]())
