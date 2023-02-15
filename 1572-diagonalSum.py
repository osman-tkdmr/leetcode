class Solution(object):
    def diagonalSum(self, mat):
        sums = 0
        for i in range(len(mat)):
            sums += mat[i][i]
            sums += mat[len(mat)-1-i][i]
        if len(mat) % 2 == 1:
            sums -= mat[len(mat)//2][len(mat)//2]
        
        return sums