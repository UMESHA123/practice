n = 4

for i in reversed(range(1, n+1)):
    for j in range(i):
        if (n-(i-1))-i == 0:
            print(i, end="")
    print()
        