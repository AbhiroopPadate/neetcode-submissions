class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return min(nums)
        else:
            l, mid, r = 0, int(len(nums)/2), len(nums)-1
            while l<mid and mid<r:
                if nums[l]<nums[mid]:
                    l = mid
                    mid = int(l + ((r-l)/2))
                    m = nums[mid+1]
                elif nums[mid]<nums[r]:
                    r = mid
                    mid = int(l + ((r-l)/2))
                    m = nums[mid+1]
        return m
                
            
            
        