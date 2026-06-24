class Solution:
    def reverseVowels(self, s: str) -> str:
        v = [c for c in s if c.lower() in "aeiou"]
        ans = ""
        for c in s:
            if c.lower() in "aeiou":
                ans += v.pop()
            else:
                ans += c  
        return ans