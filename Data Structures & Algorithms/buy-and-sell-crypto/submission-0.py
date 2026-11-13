class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        length = len(prices)

        for i in range(length):
            for j in range(i + 1, length):
                curr_profit = prices[j] - prices[i]
                if curr_profit > profit:
                    profit = curr_profit
        
        return profit