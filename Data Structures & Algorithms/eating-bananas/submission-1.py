import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #len(piles)<=h        
        #the potential rate k, will be in the range 1 to max(piles)
        #then u check piles[i]/mid and iteratively sum it. n if that sum is less<hours, that is our current best value of k. then u binary search from l to mid-1 to see if there are any better solutions
        l,r = 1,max(piles)
        res = r
        while l<=r:
            k = (l+r)//2
            ans = 0
            for p in piles:
                ans += math.ceil(p/k)
            if ans<=h:#valid solution, try to find a lower eating rate
                res = min(res,k)
                r = k-1
            else:#invalid, cuz th eating rate is too slow, look for higher eating rates
                l = k+1
        return res

        