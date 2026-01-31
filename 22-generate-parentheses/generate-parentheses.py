class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(s, open, close):
            if len(s) == 2 * n:
                res.append(s)
                return
            if open < n:
                backtrack(s + "(", open + 1, close)
            if close < open:
                backtrack(s + ")", open, close + 1)
        backtrack("", 0, 0)
        return res