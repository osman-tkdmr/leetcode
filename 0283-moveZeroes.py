class Solution(object):
    def moveZeroes(self, nums):
        k = 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i]== 0:
                nums.pop(i)
                k+=1
        while k:
            nums.append(0)
            k-=1
        return nums        