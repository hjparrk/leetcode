class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:

        def check(mid):
            total = count = 0
            for i in range(len(sweetness)):
                total += sweetness[i]
                if total >= mid:
                    total = 0
                    count += 1
            return count < k + 1

        left, right = min(sweetness), sum(sweetness)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return right


