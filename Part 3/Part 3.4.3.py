md = {}
with open('input_3.4.3.txt') as file:
    line = file.readline().strip()
    words = [w.lower() for w in line.split()]
    d = {w: words.count(w) for w in words}
    for key, value in d.items():
        if key in md.keys():
            md[key] += d[key]
        else:
            md[key] = d[key]

max_value = max(v for v in md.values())
result = [k for k in md.keys() if md[k] == max_value]
print(sorted(result)[0], max_value)
