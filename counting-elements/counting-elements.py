class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        num_set = set(arr)
        for num in arr:
            if num+1 in num_set:
                count += 1
        
        return count
            