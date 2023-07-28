def groupAnagrams(strs):
    anagramsGroups = {}
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagramsGroups:
            anagramsGroups[sorted_word].append(word)
        else:
            anagramsGroups[sorted_word] = [word]
            
    return list(anagramsGroups.values())