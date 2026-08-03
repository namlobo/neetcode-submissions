class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}#hashmap to store the count n freq
        l,r=0,0
        ans = 0
        n = len(s)
        while(r<n):
            if s[r] not in count:
                count[s[r]] = 1+count.get(s[r],0)
                r = r+1
                ans = max(ans,r-l)
            else:
                count[s[l]] -=1
                if count[s[l]]==0:
                    del count[s[l]]
                l = l+1
        return ans
        