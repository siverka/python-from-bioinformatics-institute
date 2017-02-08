'''n = 3
Зенит;3;Спартак;1
Спартак;1;ЦСКА;1
ЦСКА;0;Зенит;2
'''
n = int(input())
d = {}
total = 0
win = 1
draw = 2
lose = 3
score = 4


for i in range(n):
    key1, val1, key2, val2 = (l for l in input().split(";"))
    val1 = int(val1)
    val2 = int(val2)

    if key1 not in d:
        d[key1] = [0 for i in range(5)]
    if key2 not in d:
        d[key2] = [0 for i in range(5)]

    d[key1][total] += 1
    d[key2][total] += 1

    if val1 > val2:
        d[key1][win] += 1
        d[key2][lose] += 1

    if val2 > val1:
        d[key2][win] += 1
        d[key1][lose] += 1

    if val1 == val2:
        d[key1][draw] += 1
        d[key2][draw] += 1


for key in d:
    d[key][score] = 3*d[key][win] + d[key][draw]

for key, item in d.items():
    print(key, end=':')
    print(*item)

