class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = prices[0]
        profit = 0

        for price in prices[1:]:
            if buy > price:
                buy = price
            
            profit = max(profit, price - buy)
        
        return profit




        