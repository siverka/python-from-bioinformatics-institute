# coding=utf-8

# 1.12.1
'''a = int(input())
b = int(input())
c = int(input())

p = (a + b + c) / 2
print ((p * (p - a) * (p - b) * (p - c)) ** 0.5)
'''


# 1.12.2
'''n = int(input())
print ((-15 < n <= 12) or (14 < n < 17) or n >= 19)
'''


# 1.12.3
def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def div(x, y):
    if y == 0:
        return "Деление на 0!"
    return x / y


def mult(x, y):
    return x * y


def mod(x, y):
    if y == 0:
        return "Деление на 0!"
    return x % y


def pow(x, y):
    return x ** y


def idiv(x, y):
    if y == 0:
        return "Деление на 0!"
    return x // y


operations = {"+": add, "-": sub, "/": div, "*": mult, "mod": mod, "pow": pow, "div": idiv}


a = float(input())
b = float(input())
op = input()

print(operations[op](a, b))
