i = j = 0
        star = -1
        match = 0

        while i < len(s):
            # Case 1: direct match or '?'
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1

            # Case 2: '*' found
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1

            # Case 3: previous '*' exists → backtrack
            elif star != -1:
                j = star + 1
                match += 1
                i = match

            # Case 4: no match
            else:
                return False

        # Check remaining pattern characters
        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)
