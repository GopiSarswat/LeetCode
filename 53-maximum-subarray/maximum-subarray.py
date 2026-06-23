class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = current = nums[0]
        for num in nums[1:]:
            current = max(num, current + num)
            best = max(best, current)
        return best