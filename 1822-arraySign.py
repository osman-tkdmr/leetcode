class Solution(object):
    def arraySign(self, nums):
        if 0 in nums:
            return 0
        pro = 1
        for i in nums:
            if i == 0:return 0
            elif i < 0:
                pro = -pro
        return pro
        