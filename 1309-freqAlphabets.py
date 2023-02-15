class Solution(object):
    def freqAlphabets(self, s):
        res = ""
        i = len(s)-1
        while i+1:
            if s[i] == '#':
                res += chr(int(s[i-2:i])+96)
                i -= 3
            else:
                res += chr(int(s[i])+96)
                i-=1
        res = res[::-1]
        return res
        