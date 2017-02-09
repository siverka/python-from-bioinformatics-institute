line = ''
with open('input_3.4.2.txt') as file:
    line = file.readline().strip()

res = ''
i = 0
while i < len(line):
    char = line[i]
    j = 1
    while i + j < len(line):
        if line[i+j].isdigit():
            j += 1
        else:
            break
    num = int(''.join(line[i+1:i+j]))
    i += j
    res += char * num

with open('output_3.4.2.txt', 'w') as file:
    file.writelines(res)
