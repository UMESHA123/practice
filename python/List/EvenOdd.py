nums = [10, 21, 32, 43, 54, 65, 76, 87, 98, 109]
even = []
odd = []

for num in nums:
    if num %2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Even numbers: ", even)
print("Odd numbers: ", odd)