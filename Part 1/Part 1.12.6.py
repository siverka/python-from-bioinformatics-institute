def robot(n):
    m = n % 10
    l = n % 100
    if m == 1 and l != 11:
        print(n, "программист")
    elif 2 <= m <= 4 and l not in [12, 13, 14]:
        print(n, "программиста")
    else:
        print(n, "программистов")


robot(1)
robot(0)
robot(5)
robot(213)
robot(12)
robot(321)
robot(12)
robot(213)
