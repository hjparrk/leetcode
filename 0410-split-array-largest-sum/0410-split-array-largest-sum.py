class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def min_subarrays_required(max_sum_allowed: int) -> int:
            current_sum = 0
            splits_required = 0
            for element in nums:
                if current_sum + element <= max_sum_allowed:
                    current_sum += element
                else:
                    current_sum = element
                    splits_required += 1
            return splits_required + 1
        
        left, right = max(nums), sum(nums)
        while left <= right:
            mid = (left + right) // 2
            if min_subarrays_required(mid) <= k:
                right = mid - 1
            else:
                left = mid + 1
        
        return left