#68 Text Justification
#Difficulty - Hard
#Topics = Array String
#Time Complexity - O(n)
#Space Complexity - O(n)

from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        
        while i < len(words):
            line_len = len(words[i])
            j = i + 1
            
            while j < len(words) and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1
            
            gap_count = j - i - 1
            line = ""
            
            if j == len(words) or gap_count == 0:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            
            else:
                total_spaces = maxWidth - sum(len(word) for word in words[i:j])
                space_each = total_spaces // gap_count
                extra_spaces = total_spaces % gap_count
                
                for k in range(gap_count):
                    line += words[i + k]
                    line += " " * (space_each + (1 if k < extra_spaces else 0))
                
                line += words[j - 1]
            
            res.append(line)
            i = j
        
        return res

# Example usage:
solution = Solution()
result = solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
for line in result:
    print(f'"{line}"')
