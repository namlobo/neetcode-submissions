class Solution:

    def encode(self, strs: List[str]) -> str:
        newstr = ""
        for s in strs:
            x = len(s)
            newstr = newstr +str(x)+'#'+s
        return newstr

    def decode(self, s: str) -> List[str]:
        finalstr = []
        i = 0
        while i <len(s):
            j = i
            while s[j] !="#":
                j +=1
            length = int(s[i:j])
            finalstr.append(s[j+1:j+1+length])
            i = j+1+length
        return finalstr
                
