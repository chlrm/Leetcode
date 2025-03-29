class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        res=float('inf')
        nums.sort()
        left=0
        right=len(nums)-1
        while left<right:
            a=(nums[left]+nums[right])/2
            res=min(res,a)
            left+=1
            right-=1
        return res