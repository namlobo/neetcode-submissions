class Solution:
    def calc(self, op, a, b):
        if op == '+': return a + b
        elif op == '-': return a - b
        elif op == '*': return a * b
        elif op == '/': return int(a / b)  # truncate toward zero, not floor
        return -1
    
    def evalRPN(self, tokens: List[str]) -> int:
        operands = "+-*/"

        stack = []
        for ch in tokens:
            if ch in operands:#check if the char is an operand from the operand list you stored
                b  = stack.pop()#pop the 2 most recent elements on stack
                a = stack.pop()
                op = ch
                val = self.calc(op,a,b)
                stack.append(val)#append the calculated value on top of the stack so further calc can use this
            else:
                stack.append(int(ch)) #if integer, push onto stack
        return stack[-1]    #top element of stack contains the computed answer