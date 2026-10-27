class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy = prices[0]
        res = 0
        for i in prices:
            profit= i - minbuy
            res = max(res,profit)
            minbuy= min(minbuy,i)

        return res
        