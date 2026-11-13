class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cheapest_price = prices[0]

        for i in range(len(prices)):
            if prices[i] < cheapest_price:
                cheapest_price = prices[i]
            else:
                current_profit = prices[i] - cheapest_price
                if current_profit > profit:
                    profit = current_profit

        return profit