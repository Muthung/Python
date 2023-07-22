def isPalindrome (s):

    # Convert to lowercase
    s = s.lower()

    # Remove non-alphanumeric characters
    s = ''.join(ch for ch in s if ch.isalnum())

    # Compare with the reverse
    return s == s[::-1]
