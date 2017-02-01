def is_lucky(num):
    head = num[:len(num)//2]
    tail = num[len(num)//2:]

    a = sum(int(digit) for digit in head)
    b = sum(int(digit) for digit in tail)

    if a == b:
        print("Счастливый")
    else:
        print("Обычный")

is_lucky("090234")
is_lucky("123456")
