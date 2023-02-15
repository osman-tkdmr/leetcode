class Solution:
    def maxIceCream(self, costs, coins) :
        costs.sort()
        count = 0
        for i in costs:
            if i > coins:
                return count
            else:
                coins -= i
                count+=1
        return count