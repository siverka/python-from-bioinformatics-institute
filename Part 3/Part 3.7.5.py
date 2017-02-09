counts = {i: [] for i in range(11)}

with open("input_3.7.5.txt") as file:
    for line in file:
        c, name, h = line.strip().split()
        counts[int(c)-1].append(int(h))

for key, value in counts.items():
    print(key+1, end=' ')
    if len(value) == 0:
        print("-")
    else:
        print(sum(value)/len(value))
