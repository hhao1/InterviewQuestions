#可以用stack解，但是明显比较慢。
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        stack=[]
        profit=0
        if len(prices)<2:
            return 0
        stack.append(prices[0])
        for i in range(1,len(prices)):
            if prices[i]<stack[-1]:
                currMax=stack[-1]
                currMin=stack[-1]
                while stack:
                    currMin=stack.pop()
                stack.append(prices[i])
                profit=profit+(currMax-currMin)
            elif prices[i]>stack[-1]:
                stack.append(prices[i])
        if stack:
            currMax=stack[-1]
            currMin=stack[-1]
            while stack:
                currMin=stack.pop()
            profit=profit+(currMax-currMin)
        return profit