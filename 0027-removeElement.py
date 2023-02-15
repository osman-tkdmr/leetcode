class Solution:
    def removeElement(self, nums, val) :
        k = 0
        for i in nums:
            if i != val:
                nums[k],i = i,nums[k]
                k += 1
        return k