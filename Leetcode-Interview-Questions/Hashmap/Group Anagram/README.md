## Group Anagram

### Question 

Given an array of strings *strs*, group **the anagrams** together. You can return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#### Implementation 

To keep track of the anagram groups, the key in the hash map will be the sorted version of each word (since anagrams have the same letters when sorted), and the value will be a list of words that belong to that anagram group.

For each word, it sorts the characters and uses the sorted version as a key to the **anagramGropus** hash map.

If the key exists, it appends the current word to the list of words for the key (anagramGroups).

If the key doesn't exist, it creates a new entry in the hash map with the sorted word as the key and the current word as the initial value in the list.

The function returns the values of the **anagramGroups** hash map as a list, which represents the grouped anagrams. The order of the output groups may vary due to the unordered nature of disctionaries in python, but the anagrams within each group will always be in the same order as they appear in the input list.