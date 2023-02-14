class Solution(object):
    def longestCommonPrefix(self, strs):
        output = ""
        for x in range(len(strs[0])):
            a = strs[0][:(x+1)]
            if all(value.startswith(a) for value in strs):
                output = a
                
        return output
