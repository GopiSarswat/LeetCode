class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res = [""]
        for d in digits:
            res = [x + y for x in res for y in m[d]]
        return res