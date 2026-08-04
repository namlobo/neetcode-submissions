class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # i = 0
        # j = 0
        # temp = 0
        # while i<len(numbers):
        #     temp = target - numbers[i]
        #     j = i
        #     while temp>0 and j<len(numbers):
        #         if numbers[j]==temp:
        #             return [i+1,j+1]
        #         j = j+1
        #     i = i+1
        l,r = 0,len(numbers)-1
        ans = 0
        while l<r:
            ans = numbers[l]+numbers[r]
            if ans==target:
                return [l+1,r+1]
            elif ans<target:
                l = l+1
            elif ans>target:
                r = r-1


        