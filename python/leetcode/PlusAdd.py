def Solve(digits):
    n = len(digits)
    if n == 0:
        return []
    carry = 0
    for i in reversed(range(n)):
        if i == n-1:
            sum = carry + 1 + digits[i]
            if sum >= 10:
                carry = sum // 10
                sum = sum % 10 
        else:
            sum = carry + digits[i]
            if sum >= 10:
                carry =  sum // 10
                sum = sum % 10
        digits[i] = sum
    if carry != 0:
        digits.insert(0, carry)
    return digits

if __name__ == "__main__":
    print(Solve([9]))
