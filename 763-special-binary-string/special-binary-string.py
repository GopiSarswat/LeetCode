class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        start = 0
        substrings = []
        
        for i, ch in enumerate(s):
            if ch == '1':
                count += 1
            else:
                count -= 1
            
            # When we find a complete special substring
            if count == 0:
                # Recursively solve inner part
                inner = self.makeLargestSpecial(s[start + 1:i])
                substrings.append('1' + inner + '0')
                start = i + 1
        
        # Sort in descending order
        substrings.sort(reverse=True)
        
        return ''.join(substrings)