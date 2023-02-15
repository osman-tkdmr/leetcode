class Solution(object):
    def findErrorNums(self, nums):
        dic = [0]*(len(nums)+1)
        dub, mis = 0, 0
        for i in nums:
            dic[i]+=1
        for i in range(1,len(dic)):
            if dic[i] == 2:dup = i
            elif dic[i] == 0:mis = i
        
        return [dup,mis]
        