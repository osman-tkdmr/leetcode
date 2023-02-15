class Solution(object):
    def findJudge(self, n, trust):

        array = [0] * (n+1)
        for (a, b) in trust:
            array[a] -= 1
            array[b] += 1
        for i in range(1, len(array)):
            if array[i] == n-1:
                return i
        return -1