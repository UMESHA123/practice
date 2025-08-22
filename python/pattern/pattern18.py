n = 4

for i in range(n):
    for j in range(n-i):
        print("*", end="")
    for j in range(i*2):
        print("", end=" ")
    for j in range(n-i):
        print("*", end="")
    print()

for i in range(1,n+1):
    for j in range(i):
        print("*", end="")
    for j in range((n-i)*2):
        print("", end=" ")
    for j in range(i):
        print("*", end="")
    print()