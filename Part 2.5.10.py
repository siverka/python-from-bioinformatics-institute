#nums = [1, 3, 5, 6, 10]
nums = [int(i) for i in input().split()]
n = len(nums)
if n == 1:
    res = nums
else:
    res = [nums[(i+1) % n] + nums[(i-1) % n] for i in range(n)]

for e in res:
    print(e, end=' ')
