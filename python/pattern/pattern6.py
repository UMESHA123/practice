n = 4

for i in reversed(range(n+1)):
    for j in range(n-i):
        print("", end=" ")
    for j in range(i):
        print("*", end="")
    for j in range(i+1):
        print("*", end="")
    print("")