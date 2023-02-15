class Solution(object):
    def maximumWealth(self, accounts):
        sums =[]
        for i in accounts:
            sums.append(sum(i))
        return max(sums)