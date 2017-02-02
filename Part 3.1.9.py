def modify_list(l):
    rest = [i // 2 for i in l if i & 2 == 0]
    print(*rest)
    l.clear()
    l.extend(rest)

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
'''modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)
'''

#lst = [1, 2, 3, 4, 5, 6]
