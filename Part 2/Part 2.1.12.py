def gcd(n, m):
    a = max(n, m)
    b = min(n, m)
    r = b
    while a % b != 0:
        r = a % b
        a = b
        b = r
    return r

#print(gcd(32, 20))
#print(gcd(21, 7))
#print(gcd(5, 7))


def lcd(n, m):
    return int(n * m / gcd(n, m))


#print(lcd(7, 5))
#print(lcd(15, 15))
#print(lcd(12, 16))


a = int(input())
b = int(input())
print(lcd(a, b))
