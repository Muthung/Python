def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    charFreqS = {}
    charFreqT = {}
    
    for char in s:
        charFreqS[char] = charFreqS.get(char, 0) + 1
        
    for char in t:
        charFreqT[char] = charFreqT.get(char, 0 ) + 1
        
    return charFreqS == charFreqT