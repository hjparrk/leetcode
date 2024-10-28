class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        apples = units = 0
        for w in weight:
            units += w
            if units > 5000:
                break
            apples += 1
        return apples


        