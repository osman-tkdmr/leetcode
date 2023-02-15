class Solution(object):
    def hammingWeight(self, n):
        return str(bin(n))[2:].count('1')        