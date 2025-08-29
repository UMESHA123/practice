nums = [10,100, 100]

p1 = 0
p2 = 1
res = 1
while p2 < len(nums):
    if nums[p1] == nums[p2]:
        p2 += 1
    else:
        res += 1
        p1 += 1
        nums[p1] = nums[p2]
        p2 += 1
print(res)