#1, -3, 5, -6, -10, 13

res = 0
sum_sq = 0
while True:
    n = int(input())
    res += n
    sum_sq += n ** 2
    if res == 0:
        break
print(sum_sq)
