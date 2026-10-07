class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add open paranthesis if open<n
        #only add a closing paranthesis if closes <open
        #valid iif open==closed==n

        stack = []
        res =[]#list of valid parr combinations

        def backtrack(openn,closedn):
            if openn == closedn ==n:
                res.append("".join(stack))
                return
            if openn<n:
                stack.append("(")
                backtrack(openn+1,closedn)
                stack.pop()
            if closedn <openn:
                stack.append(')')
                backtrack(openn,closedn+1)
                stack.pop()
        backtrack(0,0)
        return res
        