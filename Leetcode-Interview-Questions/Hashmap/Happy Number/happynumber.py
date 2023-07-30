def isHappy(n):
    def GetNumber(num):
        next_sum = 0
        while num > 0:
            digit = num % 10
            next_sum += digit * digit
            num //= 10
        return next_sum
    
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = GetNumber(n)
    return n == 1