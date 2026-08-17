class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        res = 0
        max_freq =0
        count = {}#counts freq of each char in the string
        # for i in range(len(s)):
        #     count[s[i]] = 1+count.get(s[i],0)
            # if count[s[i]]>mostfreq:
            #     ch =s[i]
            #     mostfreq = count[s[i]]
        while r<len(s):
            count[s[r]]  = 1+count.get(s[r],0)

            max_freq = max(count.values())
            while (r-l+1)-max_freq>k:
                count[s[l]]-=1
                if count[s[l]]==0:
                    del count[s[l]]
                l =l+1
            res = max(r-l+1,res)
            r = r+1
        return res




        #no. of replacements is eq to the diff between len of current sub string and freq of most freq char
        # rep = 0
        # while r<len(s):
        #     rep = s[l:r]-mostfreq
        #     if rep<=k
        '''
        Algo:
        1. put all unique chars of the string into a set charSet
        2. for each c in charSet:
            - set l = 0, count = 0 (this denotes count of c inside current window)
            - slide r across the string
                > increment count when s[r]==c
                > if window needs more than k replacements, l+1, adjust count
                > update res with current valid window size'''
        # charset = set(s)
        # for c in charset:
        #     l,r = 0,0
        #     count = 0
        #     while r<len(s):
        #         if s[r]==c:
        #             count +=1
        #         if rep>k:
        #             l = l+1
            

        

        

        