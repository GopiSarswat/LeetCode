class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        top = []
        for num in nums:
            if num in top:
                continue
            top.append(num)
            top.sort(reverse=True)
            if len(top) > 3:
                top.pop()
        return top[2] if len(top) == 3 else top[0]