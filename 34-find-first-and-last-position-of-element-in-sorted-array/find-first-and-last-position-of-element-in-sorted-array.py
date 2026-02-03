class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst():
            l, r, ans = 0, len(nums) - 1, -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] >= target:
                    r = m - 1
                else:
                    l = m + 1
                if nums[m] == target:
                    ans = m
            return ans

        def findLast():
            l, r, ans = 0, len(nums) - 1, -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] <= target:
                    l = m + 1
                else:
                    r = m - 1
                if nums[m] == target:
                    ans = m
            return ans

        return [findFirst(), findLast()]
