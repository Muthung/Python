def IntegerToRoman(num):
    values = [100, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    Roman = ''

    if i in range (len(values)):
        while num >= values[i]:
            num -= values[i]
            Roman += symbols[i]

    return Roman
