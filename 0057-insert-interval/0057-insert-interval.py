class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        n = len(intervals)
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if intervals[mid][0] >= newInterval[0]:
                right = mid
            else:
                left = mid + 1
        intervals.insert(left, newInterval)

        ans = []
        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans