# Найти среднее арифетическое чисел из [a, b], которые делятся на n
def mean(a, b, n):
    nums = [i for i in range(a, b+1) if not i % n]
    return sum(nums)/len(nums)

print(mean(-5, 12, 3))

#a = int(input())
#b = int(input())

#print(mean(a, b, 3))
