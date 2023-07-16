from collections import Counter

def find_substring(s, words):
    if not s or not words:
        return []

    word_len = len(words[0])
    word_count = len(words)
    total_len = word_len * word_count
    result = []

    # Create a Counter for the words array to compare with substrings later.
    words_counter = Counter(words)

    for i in range(word_len):
        left, right = i, i
        curr_counter = Counter()

        while right + word_len <= len(s):
            curr_word = s[right:right + word_len]
            right += word_len

            if curr_word in words_counter:
                curr_counter[curr_word] += 1

                while curr_counter[curr_word] > words_counter[curr_word]:
                    # Move the left pointer to exclude the first word in the window.
                    curr_counter[s[left:left + word_len]] -= 1
                    left += word_len

                if right - left == total_len:
                    # The window size matches the total length of all words, so it's a valid substring.
                    result.append(left)

            else:
                # Reset the counters when an invalid word is found.
                curr_counter.clear()
                left = right

    return result
