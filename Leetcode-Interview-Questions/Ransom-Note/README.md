## Ransom Note 

### Question 

Given two strings *ransomNote* and *magazine*, return true if *ransomNote* can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used in *ransomNote*.

#### Implementation 

Use a hashmap (dictionary) to keep track of the counts of each character in the magazine string. 

Then, iterate through the ransomNote string and check if each character exists in the hashmap with a positive count.

If so, decrement the count and continue with the next character.

If any character is not found in the hashmap or has a count of zero, return false. 

The time complexity is *O(n + m)**, where *n* is the length of the ransomNote string, and *m* is the length of the magazine string. 

The function goes through both strings once to build the hashmap and then checks the ransomNote string against the hashmap. 

The space complexity is *O(m)* to store the hashmap, where *m* is the length of the magazine string.If you successfully iterate through all characters in the ransomNote, return true.
