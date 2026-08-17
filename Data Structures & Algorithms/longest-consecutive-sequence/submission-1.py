class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #first task is to find possible start elements , where nums[start]-1 not in nums
        numset = set(nums)
        longest = 0
        for i in range(len(nums)):
            if nums[i]-1 not in numset:
                length = 0
                while nums[i]+length in numset:
                    length +=1
                longest = max(length,longest)
        return longest
        
        #use 2 pointers l and r, l holds the value of prev, r h

        