class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = prefix_sum = 0
        counts = defaultdict(int) # sum: count
        counts[0] = 1
        for num in nums:
            prefix_sum += num
            ans += counts[prefix_sum - k]            
            counts[prefix_sum] += 1
        return ans