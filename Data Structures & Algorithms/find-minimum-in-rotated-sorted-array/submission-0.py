class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        
        #figure out no. of rotations.
        #if min is at index 0 = 6 rotations
        #min element would be at index[no. of rotations+1]
        #[5,1,2,3,4]
        #[x,r]
        if nums[0]<nums[-1]:
            #not rotated
            ans = nums[0]#best case rotated 6/0 times
        while l<r:
            mid = (l+r)//2
            # if nums[mid]<=nums[r]and nums[mid]>=nums[l]:
            #     ans = nums[mid]
            #     break
            if nums[mid]<=nums[r]:
                r = mid
            elif nums[mid]>nums[r]:
                l = mid+1
        return nums[l]

        