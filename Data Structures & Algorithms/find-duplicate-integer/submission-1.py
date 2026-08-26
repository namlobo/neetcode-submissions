class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # count = {}
        # for i in range(len(nums)):
        #     count[nums[i]] = 1+count.get(nums[i],0)
        #     if count[nums[i]]>1:
        #         ans = nums[i]
        #         break
        # return ans
        slow, fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow ==fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow ==slow2:
                break
        return slow
        