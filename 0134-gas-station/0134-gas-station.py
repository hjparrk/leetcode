class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff = [0] * n
        for i, (g, c) in enumerate(zip(gas, cost)):
            diff[i] = g - c
        
        if sum(diff) < 0: return -1
        def feasible(start, diff):
            total = 0
            for i in range(start, start + n):
                total += diff[i % n]
                if total < 0: return False
            return True

        for i in range(n):
            if diff[i] >= 0 and feasible(i, diff):
                return i
        return -1

        # for i, diff in enumerate(differences):
        #     if diff >= 0:
        #         total = 0
        #         for j in range(i, i + len(gas)):
        #             index = j % len(gas)
        #             total += differences[index]
        #             if total < 0:
        #                 break
        #         return i
        return -1