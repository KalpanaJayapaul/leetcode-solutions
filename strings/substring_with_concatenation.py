class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        from collections import Counter
        word_map = Counter(words)

        result = []

        # We only need to try word_len different offsets
        for i in range(word_len):
            left = i
            curr_count = 0
            window_map = {}

            # Move in steps of word_len
            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in word_map:
                    window_map[word] = window_map.get(word, 0) + 1
                    curr_count += 1

                    # If word appears too many times, shrink window
                    while window_map[word] > word_map[word]:
                        left_word = s[left:left + word_len]
                        window_map[left_word] -= 1
                        left += word_len
                        curr_count -= 1

                    # If window matches exactly
                    if curr_count == word_count:
                        result.append(left)

                else:
                    # Reset window
                    window_map.clear()
                    curr_count = 0
                    left = right + word_len

        return result
