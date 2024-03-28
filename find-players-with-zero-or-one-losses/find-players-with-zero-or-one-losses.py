from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        losses = defaultdict(int)
        
        for winner, loser in matches:
            losses[winner] += 0
            losses[loser] += 1
        
        no_lose, one_lose = [], []
        
        for player, count in losses.items():
            if count == 0:
                no_lose.append(player)
            if count == 1:
                one_lose.append(player)
        
        return [sorted(no_lose), sorted(one_lose)]
            
            