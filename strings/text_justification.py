class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0
        
        while i < len(words):
            # Step 1: Find words for this line
            line_length = len(words[i])
            j = i + 1
            
            while j < len(words) and line_length + 1 + len(words[j]) <= maxWidth:
                line_length += 1 + len(words[j])
                j += 1
            
            line_words = words[i:j]
            num_words = j - i
            total_chars = sum(len(word) for word in line_words)
            spaces_needed = maxWidth - total_chars
            
            # Step 2: If last line OR single word → left justify
            if j == len(words) or num_words == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            
            else:
                gaps = num_words - 1
                even_spaces = spaces_needed // gaps
                extra_spaces = spaces_needed % gaps
                
                line = ""
                for k in range(gaps):
                    line += line_words[k]
                    line += " " * (even_spaces + (1 if k < extra_spaces else 0))
                line += line_words[-1]
            
            result.append(line)
            i = j
        
        return result
