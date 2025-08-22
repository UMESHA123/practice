n = 4

for i in range(1, n+1):
    s = chr(ord('A')+i - 1)
    for j in range(i):
        print(s , end=" ")
    print()