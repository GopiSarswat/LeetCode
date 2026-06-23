class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        best = float("inf")
        ans = []
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < best:
                best = diff
                ans = [[arr[i - 1], arr[i]]]
            elif diff == best:
                ans.append([arr[i - 1], arr[i]])
        return ans