class Solution:
    def maxProfit_Better(self, prices) -> int:
        result, costIndex = 0, 0
        for sellIndex in range(len(prices)):
            profit = prices[sellIndex] - prices[costIndex]
            if profit > 0:
                result += profit
            costIndex = sellIndex
        return result

    def maxProfit(self, prices) -> int:
        result, i = 0, 0
        while i < len(prices):
            costPrice = prices[i]
            while i < len(prices) - 1 and prices[i] < prices[i + 1]:
                i += 1
            if costPrice != prices[i]:
                result += (prices[i] - costPrice)
            i += 1
        return result


s = Solution()
print(s.maxProfit([7, 6, 4, 3, 1]))
