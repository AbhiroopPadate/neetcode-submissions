class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j =0, 1
        m = 0
        while i<j and j<len(prices):
            if prices[i] < prices[j]:
                if prices[j] - prices[i] > m:
                    m = prices[j] - prices[i]
                j += 1
            else:
                i += 1
                j = i + 1
        return m

        