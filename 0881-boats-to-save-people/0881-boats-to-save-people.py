class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 1
        weights = 0
        for weight in people:
            if weight + weights > limit:
                boats += 1
                weights = 0
            weights += weight
        return boats