from heapq import *

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        nums = [-num for num in nums]
        heapify(nums)

        sums = abs(sum(nums))
        half = sums / 2
        counter = 0
        while nums:
            popped = abs(heappop(nums))
            reduced = popped / 2
            counter += 1
            if sums - reduced <= half:
                return counter
            heappush(nums, -reduced)
            sums = sums - popped + reduced
        return 0