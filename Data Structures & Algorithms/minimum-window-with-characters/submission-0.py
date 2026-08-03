class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l,r = 0,0
        m,n = len(s),len(t)
        final = ""
        counts, count = {},{}
        for i in range(n):
            count[t[i]] = 1+count.get(t[i],0)
        have,need = 0, len(count)
        while r<m:
            counts[s[r]] = 1+counts.get(s[r],0)
            if s[r] in count and counts[s[r]]==count[s[r]]:
                have +=1
            r = r+1
            while have==need:
                if len(s[l:r])<len(final) or final =="":
                    final = s[l:r]
                counts[s[l]]-=1
                if s[l] in count and counts[s[l]]<count[s[l]]:
                    have -=1
                l = l+1
        return final
        