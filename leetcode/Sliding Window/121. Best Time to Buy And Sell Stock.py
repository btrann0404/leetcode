#Using sliding window in order to calculate in a time frame
#Time Complexity: O(n) because it run through every element once
#Space Complexity: O(1) because no data structures were used

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left, right = 0, 1 #left: buy, right: sell
        max_profit = 0

        #loop until the right point reaches the end
        while right < len(prices):
            #look through all situations where left is lower than right
            print(prices[left], prices[right])
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(profit, max_profit)
            # if not move window up
            else:
                left = right
            right+=1

        return max_profit

if __name__ == "__main__":
    x = [4,6,5,3,1,7]
    print(Solution().maxProfit(x))
