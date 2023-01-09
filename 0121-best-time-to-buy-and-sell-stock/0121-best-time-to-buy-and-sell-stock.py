class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy_price = prices[0]
        for price in prices:
            if price < min_buy_price:
                min_buy_price = price
                continue
            if price - min_buy_price > max_profit:
                max_profit = price - min_buy_price
        return max_profit