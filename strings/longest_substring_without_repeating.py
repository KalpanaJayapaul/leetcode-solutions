class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = {}
        max_length = 0
        start = 0

        for end, char in enumerate(s):
            if char in seen and seen[char] >= start:
                start = seen[char] + 1

            seen[char] = end
            max_length = max(max_length, end - start + 1)

        return max_length
