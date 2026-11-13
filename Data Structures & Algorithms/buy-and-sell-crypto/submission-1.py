class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        length = len(prices)
        cheapest_price = prices[0]

        for i in range(length):
            if prices[i] < cheapest_price:
                cheapest_price = prices[i]
                print("cheapest price: "+ str(cheapest_price))
            else:
                current_profit = prices[i] - cheapest_price
                print("current_profit: "+ str(current_profit))
                if current_profit > profit:
                    profit = current_profit

        return profit