class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Find Pivot
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        # Configure Searching Range
        pivot = left
        if pivot == 0:
            left, right = 0, len(nums) - 1
        elif target >= nums[0] and target <= nums[pivot - 1]:
            left, right = 0, pivot - 1
        else:
            left, right = pivot, len(nums) - 1
        
        # Binary Search
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
            



