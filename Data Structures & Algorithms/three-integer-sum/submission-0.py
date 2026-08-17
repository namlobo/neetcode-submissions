class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # i,j = 0, len(nums)-1
        # ans = []
        # while i<j:
        #     curr =nums[i]+nums[j]
        #     k=0
        #     while k<len(nums)-1:
        #         if nums[k]+curr ==0 and k!=i and k!=j:
        #             ans.append([nums[i],nums[j],nums[k]])
        #         k = k+1
        #     i = i+1
        #     j = j-1
                
        # return ans
        
        #logic can be pick an index i, as target and perform regular two sum operations for j and k index
        nums.sort()
        ans = []
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            
            l,r = i+1,len(nums)-1
            while l<r:
                threesum = a+nums[l]+nums[r]
                if threesum>0:
                    r-=1
                elif threesum<0:
                    l +=1
            # curr = nums[l]+nums[r]
                else:
                    ans.append([a,nums[l],nums[r]])
                    l = l+1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return ans
            # if curr>0:
            #     r = r-1
            # elif curr<0:
            #     l = l+1



            


        