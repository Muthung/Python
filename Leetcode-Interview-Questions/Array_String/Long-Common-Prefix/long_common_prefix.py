def longCommonPrefix(strs):
    if not strs:
        return ""

    # The minimum length string in the array
    len_min = min(len(s) for s in strs)

    # Iterate over the characters of the first string
    for i in range(len_min):

        # Check if all other strings have the same character at the current position
        for j in range(1, len(strs)):
            if strs[j][i] != strs[0][i]:

                # Characters don't match, return the prefix found so far
                return strs[0][:i]

    return strs[0][:len_min]
