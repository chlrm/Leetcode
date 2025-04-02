class Solution(object):
    def findPeakElement(self, nums):
        a=[max(nums)]
        for i in range(0,len(nums)+1):
            if nums[i] in a:
                return i