class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for x in nums:
            # If x is even, it's impossible
            if x % 2 == 0:
                ans.append(-1)
                continue

            # Count trailing 1s in binary representation of x
            k = 0
            temp = x
            while temp & 1:
                k += 1
                temp >>= 1

            # Compute smallest valid ans[i]
            a = x - (1 << (k - 1))
            ans.append(a)

        return ans