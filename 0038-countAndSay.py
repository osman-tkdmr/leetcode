class Solution:
    def countAndSay(self, n):            
        if n == 1: return "1"
        res = "1"
        for _ in range(n-1):
            let, temp, count = res[0], "", 0
            for i in res:
                if let == i:
                    count += 1
                else:
                    temp += str(count) + let
                    let = i
                    count = 1
            temp += str(count) + let
            res = temp
        return res