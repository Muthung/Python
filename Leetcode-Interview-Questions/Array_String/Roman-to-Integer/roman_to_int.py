def RomanToInt(s):
    values_symbol = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0

    n = len(s)

    for i in range(s):
        value = values_symbol[s[i]]

        if i < n - 1 and values_symbol[s[i + 1]] > value:
            result -= value

        else:
            result += value
    return result
