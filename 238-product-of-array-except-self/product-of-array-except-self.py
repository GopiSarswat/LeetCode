class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # a = []
        # for i in range(len(nums)):
        #     x = 1
        #     for j in range(len(nums)):
        #         if(i == j):
        #             continue
        #         else:
        #             x *= nums[j]
        #     a.append(x)
        # return a
        x = [0] * len(nums)
        pre = [1] * len(nums)
        post = [1] * len(nums)
        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] * nums[i - 1]
        print(pre)
        for i in range(len(nums) - 2, -1, -1):
            post[i] = post[i + 1] * nums[i + 1]
        print(post)
        for i in range(len(nums)):
            x[i] = pre[i] * post[i]
        
        return x    