class Solution(object):
    def checkStraightLine(self, coordinates):
        if len(coordinates) == 2:
            return True
        for i in range(len(coordinates)-2):
            s = (coordinates[i][0]-coordinates[i+1][0])*(coordinates[i+2][1]-coordinates[i+1][1])-(coordinates[i+2][0]-coordinates[i+1][0])*(coordinates[i][1]-coordinates[i+1][1])
            if s != 0:return False
        return True