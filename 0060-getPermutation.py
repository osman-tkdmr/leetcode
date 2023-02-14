import math
def getPermutation(n, k):
    stToRet = ""
    lst  = [str(i) for i in range(1,n+1)]
    
    while len(lst):
        n = len(lst)
        n1Fac = math.factorial(n - 1)
        idxToRem = k / n1Fac-1 if (k % n1Fac == 0) else k / n1Fac
        stToRet += lst.pop(idxToRem)
        k = k % n1Fac
    return stToRet
