def modify_list(l):
    rest = [i // 2 for i in l if i % 2 == 0]
    l.clear()
    l.extend(rest)
