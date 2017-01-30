# 1.10.5
a = int(input("a "))
b = int(input("b "))
h = int(input("h "))

def sleep(a, b, h):
    if h < a:
        print("Nedosyp")
    elif h > b:
        print("Peresyp")
    else:
        print("Norm")

# 1.10.6
def is_leap(n):
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        print("leap")
    else:
        print("not leap")


print ("test")
is_leap(2100)
is_leap(2000)
