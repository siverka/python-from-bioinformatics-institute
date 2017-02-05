def table(a, b, c, d):
    print('', end='\t')
    for i in range(c, d+1):
        print(i, end='\t')
    print()

    for i in range(a, b+1):
        print(i, end='\t')
        for j in range(c, d+1):
            print(i*j, end='\t')
        print()


table(7, 10, 5, 6)
print()
table(5, 5, 6, 6)
print()
table(1, 3, 2, 4)
