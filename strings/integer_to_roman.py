class Solution:
    def intToRoman(self, num):
        roman = []
        
        values = [
            (1000, "M"),
            (900,  "CM"),
            (500,  "D"),
            (400,  "CD"),
            (100,  "C"),
            (90,   "XC"),
            (50,   "L"),
            (40,   "XL"),
            (10,   "X"),
            (9,    "IX"),
            (5,    "V"),
            (4,    "IV"),
            (1,    "I")
        ]

        for value, symbol in values:
            while num >= value:
                roman.append(symbol)
                num -= value

        return "".join(roman)

'''
How it works (example: 1994)

Start with 1994:

1000 → M → remaining 994

900 → CM → remaining 94

90 → XC → remaining 4

4 → IV → remaining 0

Result:

"MCMXCIV"
Example outputs
3749 → MMMDCCXLIX
58   → LVIII
1994 → MCMXCIV
'''
