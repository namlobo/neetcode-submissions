class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = 1+count.get(nums[i],0)
            if count[nums[i]]>1:
                ans = nums[i]
                break
        return ans
        