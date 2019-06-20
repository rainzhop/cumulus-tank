# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        candidate_profit = [0]
        min_val = prices[0]
        max_val = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min_val:
                max_val = max_val - (min_val - prices[i])
                min_val = prices[i]
            if prices[i] > max_val:
                max_val = prices[i]
                candidate_profit.append(max_val - min_val)
        return max(candidate_profit)


if __name__ == '__main__':
    prices = [8,9,2,5]
    s = Solution()
    print s.maxProfit(prices)
