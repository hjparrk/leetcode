class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        mapping = {}

        for num in nums2:
            
            while stack and stack[-1] < num:
                popped = stack.pop()
                mapping[popped] = num

            stack.append(num)
        
        return [mapping.get(num, -1) for num in nums1]