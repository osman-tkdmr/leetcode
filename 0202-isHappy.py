class Solution(object):
    def isHappy(self, n):
        def allPro(num):
            total = 0
            while num > 0:
                digit = num % 10
                num = num//10
                total += digit**2
            return total
        list1 = []
        while n != 1 and n not in list1:
            list1.append(n)
            n = allPro(n)
        
        return n == 1