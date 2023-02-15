class Solution(object):
    def minCost(self, colors, neededTime):
        
        temp_max = 0
        total_time = 0
        
        for i in range(len(colors)):
            if i  != 0 and colors[i] != colors[i - 1]:
                temp_max = 0

            total_time += min(temp_max, neededTime[i])
            temp_max = max(temp_max, neededTime[i])

        return total_time
    
        