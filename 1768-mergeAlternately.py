class Solution(object):
    def mergeAlternately(self, word1, word2):
        dif = abs(len(word1)-len(word2))
        ek =""
        if dif != 0:
            if len(word1)>len(word2):
                ek = word1[-dif:]
            else:
                ek =word2[-dif:]
        
        w = ""
        for i in list(zip(word1,word2)):
            w+=i[0]
            w+=i[1]
        return w+ek
        