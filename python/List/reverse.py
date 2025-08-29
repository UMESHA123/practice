nums = [10,10, 100, 200, 1, 20, 30, 40, 50, 60, 60, 110]

nums.reverse()
print(nums)

temp = reversed(nums)
print(list(temp))
print(nums)  # nums remains unchanged

print(nums[::-1])  # slicing to reverse the list
print(nums)  # nums remains unchanged
 
nums = [10,20, 30, 40, 50, 50]

left = 0
right = len(nums) - 1
while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1
print(nums)