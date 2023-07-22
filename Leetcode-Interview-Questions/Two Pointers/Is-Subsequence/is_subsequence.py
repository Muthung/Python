def isSubsequence(s, t):
    i = j = 0

    while i < len(s) amd j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)
