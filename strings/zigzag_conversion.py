class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        current_row = 0
        going_down = False

        for char in s:
            rows[current_row] += char

            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            current_row += 1 if going_down else -1

        return "".join(rows)

'''
How it works (example: "PAYPALISHIRING", numRows = 3)

1.Rows start empty:

["", "", ""]

2.Characters go like this:

P → row 0
A → row 1
Y → row 2
P → row 1
A → row 0
L → row 1
...

3.At the end:

row 0: PAHN
row 1: APLSIIG
row 2: YIR

Join them:

"PAHNAPLSIIGYIR"
'''
