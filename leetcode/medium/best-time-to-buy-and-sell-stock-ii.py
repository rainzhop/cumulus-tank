# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
#
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit.
# You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times).
# However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        profit_list = []
        min_val = prices[0]
        max_val = prices[0]
        tend = 0 # 0:down, 1:up
        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                # go down
                if tend == 1:
                    max_val = prices[i - 1]
                    profit_list.append(max_val - min_val)
                tend = 0
                pass
            if prices[i] > prices[i - 1]:
                # go up
                if tend == 0:
                    min_val = prices[i - 1]
                tend = 1
                pass
        if tend == 1:
            profit_list.append(prices[i] - min_val)
        return sum(profit_list)


if __name__ == '__main__':
    prices = [8,9,2,5]
    s = Solution()
    print s.maxProfit(prices)
