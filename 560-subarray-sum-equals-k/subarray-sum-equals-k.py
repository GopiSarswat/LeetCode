class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        prefix = 0
        ans = 0
        for num in nums:
            prefix += num
            ans += counts[prefix - k]
            counts[prefix] += 1
        return ans