class Solution(object):
    def finalPrices(self, prices):
        n = len(prices)
        stack = []
        result = prices[:]

        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:
                j = stack.pop()
                result[j] -= prices[i]
            stack.append(i)
        return result