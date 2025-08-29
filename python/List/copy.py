nums = [10, 20, 30, 40, 50]

res = nums[:]

print("Original List:", nums)
print("Copied List:", res)
print(nums is res) # False because they are different objects
print(nums == res) # True because they have same content
print()
t1 = (1, 2, 3)
t2 = t1[:]
print(t1 is t2) # True because they are same objects
print(t1 == t2) # True because they have same content
print()
s1 = "Hello"
s2 = s1[:]
print(s1 is s2) # True because they are same objects
print(s1 == s2) # True because they have same content

