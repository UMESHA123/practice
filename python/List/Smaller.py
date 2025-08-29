nums = [8, 15, 24, 7, 3, 12, 18, 5, 30, 11]
x = 16
smaller = []

for num in nums:
    if num < x:
        smaller.append(num)

print("Numbers smaller than", x, "are:", smaller)
print("Count of numbers smaller than", x, "is:", len(smaller))