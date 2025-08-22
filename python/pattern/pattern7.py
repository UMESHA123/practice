n = 4
for i in range(n+1):
    #display space before printing *
    #print n *'s at left
    #print (n+1) *'s at right
    for j in range(n-i):
        print("", end=" ")
    for j in range(i):
        print("*", end="")
    for j in range(i+1):
        print("*", end="")
    print()

for i in reversed(range(n+1)):
    for j in range(n-i):
        print("", end=" ")
    for j in range(i):
        print("*", end="")
    for j in range(i+1):
        print("*", end="")
    print("")