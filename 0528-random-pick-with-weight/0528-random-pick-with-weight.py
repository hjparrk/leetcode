class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []

        curr = 0
        for weight in w:
            curr += weight
            self.prefix_sum.append(curr)
        
        self.total = self.prefix_sum[-1]

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        index = bisect_left(self.prefix_sum, target)
        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()