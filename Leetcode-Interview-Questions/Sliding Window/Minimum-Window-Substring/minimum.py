def min_window_substring(s, t):
    # Initialize the frequency dictionaries for characters in s and t
    char_count_s = {}
    char_count_t = {}
    for char in t:
        char_count_t[char] = char_count_t.get(char, 0) + 1

    # Function to check if the window contains all characters from t
    def contains_all_chars():
        for char, count in char_count_t.items():
            if char_count_s.get(char, 0) < count:
                return False
        return True

    left, right = 0, 0
    min_window = ""
    min_length = float('inf')

    while right < len(s):
        # Expand the window to the right
        char_count_s[s[right]] = char_count_s.get(s[right], 0) + 1
        right += 1

        # Contract the window from the left if it contains all characters from t
        while contains_all_chars() and left < right:
            window_length = right - left
            if window_length < min_length:
                min_window = s[left:right]
                min_length = window_length

            char_count_s[s[left]] -= 1
            left += 1

    return min_window
