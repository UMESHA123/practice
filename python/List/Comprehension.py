l1 = [x for x in range(1, 11)]
print(l1)

l2 = [x*x for x in range(1, 11)]
print(l2)

l3 = [x for x in range(1, 11) if x % 2 == 0]
print(l3)

l4 = [x*x for x in range(1, 11) if x % 2 == 0]
print(l4)

l5 = [x if x % 2 == 0 else x*x for x in range(1, 11)]
print(l5)