n = 4

for i in range(1, n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    for k in range(2):
        for j in range(2*(n-i)):
            print("", end=" ")
    
    for j in reversed(range(1, i+1)):
        print(j, end=" ")
    print()