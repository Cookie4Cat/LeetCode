class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum([profit for profit in [prices[i+1]-prices[i] for i in range(len(prices)-1)] if profit>0])

if __name__ == '__main__':
    prices = [1,5,-1,2,5,4,9]
    solution = Solution()
    print(solution.maxProfit(prices))