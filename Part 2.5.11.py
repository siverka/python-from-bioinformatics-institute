#nums = [4, 8, 0, 3, 4, 2, 0, 3]
#nums = [10]
#nums = [1, 1, 2, 2, 3, 3]
#nums = [1, 1, 1, 1, 1, 2, 2, 2]
nums = [int(i) for i in input().split()]

nums.sort()
#print(nums)
rep = [nums.count(e) for e in nums]
#print(rep)
i = 0
while i < len(nums):
    if rep[i] > 1:
        print(nums[i], end=' ')
        i += rep[i]
    else:
        i += 1
