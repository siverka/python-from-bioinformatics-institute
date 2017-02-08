'''4
север 10
запад 20
юг 30
восток 40
'''

n = int(input())
d = {'север': 0, 'запад': 0, 'юг': 0, 'восток': 0}
for i in range(n):
    direction, steps = input().split()
    d[direction] += int(steps)

print(d['восток'] - d['запад'], d['север'] - d['юг'])
