class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) > ceil(hour):
            return -1

        def check(speed):
            time = 0
            for distance in dist:
                time = ceil(time)
                time += (distance / speed)
            return time <= hour
        
        left, right = 1, 10**7
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
