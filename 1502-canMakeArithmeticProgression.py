class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort(reverse = True)
        diff = arr[0] - arr[1]
        for i in range(len(arr)-1):
            if arr[i] - arr[i+1] != diff:
                return False
        return True