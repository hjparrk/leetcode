class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        def binary_search(arr, target):
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            return left

        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        ans = []
        for query in queries:
            i = binary_search(nums, query)
            ans.append(i)
        return ans
        