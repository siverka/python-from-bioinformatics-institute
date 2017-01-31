#lst = [5, 8, 2, 7, 8, 8, 2, 4, 10]
#x = 8
#x = 10

lst = [int(i) for i in input().split(' ')]
x = int(input())

if lst.count(x) == 0:
    print("Отсутствует")
else:
    start = 0
    for i in range(lst.count(x)):
        index = lst.index(x, start, len(lst))
        print(index, end=" ")
        start = index + 1
