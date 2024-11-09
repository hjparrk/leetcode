class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff, ans = float('inf'), []
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            if diff == min_diff:
                ans.append([arr[i], arr[i + 1]])
            if diff < min_diff:
                ans = []
                min_diff = diff
                ans.append([arr[i], arr[i + 1]])
        return ans
