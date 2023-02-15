class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        groups = {char: char for char in "abcdefghijklmnopqrstuvwxyz"}
        
        def find(x):
            if x != groups[x]:
                groups[x] = find(groups[x])  # path compression, if needed
            return groups[x]
        
        for a, b in zip(s1, s2): 
            x, y = find(a), find(b)
            groups[max(x, y)] = min(x, y)  # make union of letter pairs from `s1` and `s2`, lowest value ranked highest
        
        return "".join(find(char) for char in baseStr)