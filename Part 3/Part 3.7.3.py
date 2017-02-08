'''3
a
bb
cCc
2
a bb aab aba ccc
c bb aaa
'''


nd = int(input())
d = set()

for i in range(nd):
    d.update([input().lower()])

nl = int(input())
l = set()
for i in range(nl):
    l.update([e.lower() for e in input().split()])

diff = l.difference(d)
print(*diff, sep='\n')
