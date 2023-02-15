class Solution:
    def maximumBags(self, capacity, rocks, additionalRocks):
        fark = [0] * len(capacity)
        res = 0
        
        for i in range(len(capacity)):
            fark[i] = capacity[i] - rocks[i]
        fark.sort()
        
        for i in range(len(fark)):
            if fark[i] > additionalRocks:
                break
                
            additionalRocks -= fark[i]
            res += 1
        
        return res