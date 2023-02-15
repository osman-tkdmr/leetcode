class Solution(object):
    def average(self, salary):
        return (sum(salary)-max(salary)-min(salary)) / float(len(salary)-2)
