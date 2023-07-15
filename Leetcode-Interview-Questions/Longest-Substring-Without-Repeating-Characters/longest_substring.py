def lengthOfLongestSubstring(s):
    start = 0
    end = 0
    max_length = 0
    seen = set()

    while end < len(s):
        if s[end] not in seen:
            seen.add(s[end])
            end += 1
            max_length = max(max_length, end - start)
        else:
            seen.remove(s[start])
            start += 1

    return max_length
