import collections

class Solution:
	def largestOverlap(self, img1, img2) :
		overlapDict = collections.defaultdict(int)
		A = []
		B = []
		ans = 0
		for i in range(len(img1)):
			for j in range(len(img1[0])):
				if img1[i][j] == 1:
					A.append((i, j))
				if img2[i][j] == 1:
					B.append((i,j))
		for a in A:
			for b in B:
				translation = (a[0]-b[0], a[1]-b[1])
				overlapDict[translation] += 1
				ans = max(ans, overlapDict[translation])
		return ans