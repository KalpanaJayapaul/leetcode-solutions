class Solution:
    def isNumber(self, s):
        s = s.strip()
        
        seen_digit = False
        seen_dot = False
        seen_e = False
        
        for i, char in enumerate(s):
            
            if char.isdigit():
                seen_digit = True
            
            elif char in ['+', '-']:
                # Sign allowed only at start or just after e/E
                if i > 0 and s[i - 1] not in ['e', 'E']:
                    return False
            
            elif char == '.':
                # Dot only allowed once and before exponent
                if seen_dot or seen_e:
                    return False
                seen_dot = True
            
            elif char in ['e', 'E']:
                # e must appear once and after at least one digit
                if seen_e or not seen_digit:
                    return False
                seen_e = True
                seen_digit = False  # must have digits after e
            
            else:
                return False
        
        return seen_digit
