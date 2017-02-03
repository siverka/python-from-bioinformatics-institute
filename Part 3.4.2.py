with open('input_3.4.2.txt') as file:
    line = file.readline().strip()
    print(line)


inline = 'a3b4c2e10b1'
res = ''
for i in range(len(inline)):
    sym = ''
    ch = inline[i]
    n = inline[i+1]
