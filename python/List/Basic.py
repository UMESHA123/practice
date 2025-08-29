l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(l)
print(l[0])
print(l[-1])
print(l[0:5])

l.append(110)
print(l)

l.insert(1,15)
print(l)

print(15 in l)
print(l.count(15))

l.remove(15) # check before removing if element is not present in list it reaises value error 
print(l)

l.pop() # removes last element before check if list is not empty else raises index error
print(l)

l.pop(0)
print(l)

l[0] = 5
print(l)

l.sort()
print(l)

l.reverse()
print(l)

print(l.index(50))
print(l.index(50, 3))
print(l.index(50, 3, 8))

l2 = [200, 300]
l.extend(l2)
print(l)

del l[0]
del l[2:4]
print(l)

print(max(l))
print(min(l))
print(len(l))
print(sum(l))


l.clear()
print(l)

