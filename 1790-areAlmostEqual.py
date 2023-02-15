class Solution(object):
    def areAlmostEqual(self, s1, s2):
        if sorted(s1)!=sorted(s2):
            return False
        if s1 == s2 :return True
        count = 0
        for i in range(len(s2)):
            if s1[i] != s2[i]:
                count+=1
            
        return count == 2 or count ==0
        