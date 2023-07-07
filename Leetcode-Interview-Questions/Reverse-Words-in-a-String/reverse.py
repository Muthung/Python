def reverseWords(s):

    # Trim leading and trailing spaces
    s = s.strip()

    # Split the string into words
    words = s.split()

    # Reverse the array of words
    words = words[::-1]

    #Join the reversed words into a string
    string_reverse = ' '.join(words)

    return string_reverse
