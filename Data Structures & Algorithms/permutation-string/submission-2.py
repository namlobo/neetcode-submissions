from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #its a fixed sliding window problem,
        S1 = Counter(s1)
        S2 = Counter(s2)
        window = len(s1)
        l,r = 0,window-1
        while r<len(s2):
            if Counter(s2[l:r+1])==S1:
                return True
            l = l+1
            r = r+1
        return False
        
        
        '''
        approach can be using hashmap to count the chars in s2, and then if the counts1[s1[i]]<=counts2[s[i]]'''

        