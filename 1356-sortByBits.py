class Solution(object):
    def sortByBits(self, arr):
        arr.sort()
        for i in range(len(arr)-1):
            for j in range(i,len(arr)):
                if str(bin(arr[i])).count('1') <= str(bin(arr[j])).count('1'):
                    arr[i], arr[j] = arr[j],arr[i]
        arr.reverse()
        return arr