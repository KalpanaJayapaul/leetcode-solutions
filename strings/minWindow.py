class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        target = {}
        for char in t:
            target[char] = target.get(char, 0) + 1

        required = len(target)
        formed = 0

        window = {}

        left = 0
        right = 0

        min_len = float("inf")
        min_left = 0

        while right < len(s):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in target and window[char] == target[char]:
                formed += 1

            while left <= right and formed == required:

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left

                left_char = s[left]
                window[left_char] -= 1

                if left_char in target and window[left_char] < target[left_char]:
                    formed -= 1

                left += 1

            right += 1

        if min_len == float("inf"):
            return ""

        return s[min_left:min_left + min_len]
