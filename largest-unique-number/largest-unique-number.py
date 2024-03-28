from collections import defaultdict

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        ans = -1
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        l = [k for k in count if count[k] == 1]
        return max(l) if len(l) else -1
    
#         c = collections.Counter(nums)

#         res = - 1
#         for k in c:
#             if c[k] == 1:
#                 res = max(res, k)
        
#         return res
    
#         s1 = set()
#         s2 = set()

#         for n in nums:
#             if n not in s1 and n not in s2:
#                 s1.add(n)
#             elif n not in s2:
#                 s1.remove(n)
#                 s2.add(n)
        
#         return max(s1) if s1 else -1
                