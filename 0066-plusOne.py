class Solution:
    def plusOne(self, digits) :
        num = 0
        n = 0
        liste = []
        for i in digits[::-1]:
            num += i * (10**n)
            n += 1
        num += 1
        num = str(num)
        for i in num:
            liste.append(int(i))
        return liste