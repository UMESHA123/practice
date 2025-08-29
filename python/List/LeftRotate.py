nums = [10, 20, 30, 40, 50, 60]
temp = nums[0]

for i in range(1, len(nums)):
    nums[i-1] = nums[i]
nums[-1] = temp
print(nums)