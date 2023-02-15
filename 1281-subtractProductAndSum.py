class Solution(object):
    def subtractProductAndSum(self, n):
        pro = 1
        sum = 0
        for i in str(n):
            pro *= int(i) % 10
            sum += int(i) % 10
            
        return pro - sum
        