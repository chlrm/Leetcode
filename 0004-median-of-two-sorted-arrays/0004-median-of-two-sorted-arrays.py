class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        m=len(nums1)//2
        if len(nums1)%2!=0:
            return nums1[m]
        else:
            return (nums1[m-1]+nums1[m])/2.0