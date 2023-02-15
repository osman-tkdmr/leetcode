class Solution:
    def topKFrequent(self, words, k) :
        dict = {} ; res = []
        s = list(set(words))
        s.sort()
        for i in s:
            dict[i]  = words.count(i)
        dict[''] = 0
        for _ in range(k):
            tmp = ''
            for i in dict:
                if dict[i] > dict[tmp]:
                    tmp = i
            res.append(tmp)
            dict.pop(tmp)
        return res