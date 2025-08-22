n = 5

for i in range(1, n+1):
    s = chr(65) 
    for j in reversed(range(i)):
        print(chr(ord(s)+n-j-1), end=" ")
    print()