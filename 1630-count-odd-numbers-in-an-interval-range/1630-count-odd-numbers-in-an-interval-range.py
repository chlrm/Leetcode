class Solution(object):
    def countOdds(self, low, high):
        c=(high-low+1)
        if c%2==0:
            return c//2
        return c//2+(low%2)