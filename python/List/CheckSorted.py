def Check(nums):
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            return False
    return True

nums = [10, 10, 30, 40, 50, 60, 70, 80, 90, 100]
res = Check(nums)
print(res)