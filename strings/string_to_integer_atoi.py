class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)
        sign = 1
        num = 0

        # 1. Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # 3. Read digits
        while i < n and s[i].isdigit():
            num = num * 10 + (ord(s[i]) - ord('0'))

            # 4. Clamp early to avoid overflow
            if sign * num <= -2**31:
                return -2**31
            if sign * num >= 2**31 - 1:
                return 2**31 - 1

            i += 1

        return sign * num
