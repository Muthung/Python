def lengthOfLastWord(s):

    # Trim the input string
    s = s.strip()

    #Find the index of the last space
    last_space_index = s.rfind(' ')

    # Extract the substring from the last space + 1 to the end
    last_word = s[last_space_index + 1:]

    # Return the length of the last word
    return len(last_word)
