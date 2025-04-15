class Solution(object):
    def findClosest(self, x, y, z):
        if x>z:
            x-=z
        else:
            x=-(x-z)
        if y>z:
            y-=z
        else:
            y=-(y-z)
        if x==y:
            return 0
        elif x<y:
            return 1
        return 2