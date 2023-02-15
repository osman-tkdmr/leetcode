class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort(reverse = True)
        for i in range(len(nums)-2):
            if nums[i + 2] + nums[i + 1] > nums[i]:
                return sum(nums[i:i+3])
        return 0