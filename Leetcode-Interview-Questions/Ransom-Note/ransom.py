def can_construct(ransomNote, magazine):
    # Create a hashmap to store character counts in the magazine
    char_count = {}

    # Count characters in the magazine string
    for char in magazine:
        char_count[char] = char_count.get(char, 0) + 1

    # Check if ransomNote can be constructed using characters from magazine
    for char in ransomNote:
        if char in char_count and char_count[char] > 0:
            char_count[char] -= 1
        else:
            return False

    return True
