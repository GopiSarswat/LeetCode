class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans = 0
        while any(nums[i] > nums[i+1] for i in range(len(nums)-1)):
            i = min(range(len(nums)-1), key=lambda k: nums[k] + nums[k+1])
            nums = nums[:i] + [nums[i] + nums[i+1]] + nums[i+2:]
            ans += 1
        return ans