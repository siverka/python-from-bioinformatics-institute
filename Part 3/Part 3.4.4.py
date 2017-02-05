with open("input_3.4.4.txt") as file:
    content = file.readlines()

data = [[int(z) for z in x.strip().split(';')[1:]] for x in content]

first = []
second = []
third = []

with open('output_3.4.4.txt', 'w') as file:
    for row in data:
        first.append(row[0])
        second.append(row[1])
        third.append(row[2])
        file.write(str(sum(row) / len(row)) + '\n')

    file.write(str(sum(first) / len(first)) + ' ')
    file.write(str(sum(second) / len(second)) + ' ')
    file.write(str(sum(third) / len(third)) + ' ')

