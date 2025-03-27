class Solution(object):
    def intersect(self, nums1, nums2):
        box = Counter(nums1)
        res = []

        for num in nums2:
            if box[num] > 0:
                res.append(num)
                box[num] -= 1
        return res