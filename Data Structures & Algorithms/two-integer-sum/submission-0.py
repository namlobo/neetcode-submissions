class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i,j = 0,len(nums)-1
        # while(i<j):
        #     if nums[i]+nums[j]==target:
        #         return [i,j]
        #     i = i+1
        #     j = j-1
        for i in range(len(nums)-1):
            for j in range(len(nums)-1,i,-1):
                if nums[i]+nums[j]==target:
                    return [i,j]
            
        