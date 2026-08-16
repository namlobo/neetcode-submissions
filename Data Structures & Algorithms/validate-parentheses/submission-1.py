class Solution:
    def isValid(self, s: str) -> bool:
        #basic algo is , when its an opening bracket, stack.push(s[i])
        #when char is in matching dict, and stack is not empty and top of stack!=mapping, you pop the element from the stack , cuz the match has been found
        #else if its opening paranthesis you push into the stack
        stack =[]
        matching = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for i in range(len(s)):
            if s[i] in matching:#means its a closing parenthesis
                if not stack or stack[-1]!=matching[s[i]]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(s[i])
        if not stack:
            return True
        else:
            return False
        