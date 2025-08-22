n = 4
for i in range(n):
    print("*", end="")
print()
for i in range(2,n):
    print("*", end="")
    for j in range(n-2):
        print("", end=" ")
    print("*")
for i in range(n):
    print("*", end="")
print()