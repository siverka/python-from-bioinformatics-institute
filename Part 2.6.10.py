mtrx = []
while True:
    input_str = input()
    if input_str == "end":
        break
    else:
        mtrx.append([int(i) for i in input_str.split()])

#mtrx = [[9, 5, 3], [0, 7, -1], [-5, 2, 9]]
#mtrx = [[1]]

m = len(mtrx)   #m rows
n = len(mtrx[0])    #n cols
res = [[0 for i in range(n)] for j in range(m)]

for j in range(m):
    for i in range(n):
        res[j][i] += mtrx[(j-1) % m][i]
        res[j][i] += mtrx[(j+1) % m][i]
        res[j][i] += mtrx[j][(i-1) % n]
        res[j][i] += mtrx[j][(i+1) % n]

for j in range(m):
    for i in range(n):
        print(res[j][i], end=' ')
    print()
