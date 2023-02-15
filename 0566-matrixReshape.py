class Solution(object):
    def matrixReshape(self, mat, r, c):
        arr = []
        for i in mat:
            for j in i:
                arr.append(j)
        if r*c != len(arr):
            return mat
        res =[]
        for i in range(r):
            res.append([])
        k=0

        for i in range(r):
            for j in range(c):
                res[i].append(arr[k])
                k+=1
        return res