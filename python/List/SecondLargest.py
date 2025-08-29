# nums = [10,10, 100, 200, 1, 20, 30, 40, 50, 60, 60, 110]
nums = [20, 20, 10]

largest = -1
second_largest = -1
for num in nums:
    if num > largest:
        second_largest = largest
        largest = num
    elif num == largest:
        continue
    elif num < largest and num > second_largest:
        second_largest = num


    
print("Largest:", largest)
print("Second Largest:", second_largest)