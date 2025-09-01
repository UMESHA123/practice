def removeElement(nums, val):
    n = len(nums)
    p1 = 0
    p2 = 0
    res = 0
    while p2 < n:
        if nums[p1] == val:
            if nums[p2] != val:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                res += 1
                p1 += 1
            p2 += 1
        else:
            res += 1
            p1 += 1
            p2 += 1
    return res 

nums = [0,1,2,2,3,0,4,2]
res = removeElement(nums, 2)
for i in range(res):
    print(nums[i])
