class MedianFinder:

    def __init__(self):
        self.liste = []

    def addNum(self, num):
        self.liste.append(num)

    def findMedian(self) -> float:
        n = len(self.liste)
        self.liste.sort()
        if(n%2):
            return self.liste[n//2]
        else:
            return (self.liste[n//2]+self.liste[n//2 -1])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()