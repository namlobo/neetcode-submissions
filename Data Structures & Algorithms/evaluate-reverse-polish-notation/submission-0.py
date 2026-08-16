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
            if ch in operands:
                b  = stack.pop()
                a = stack.pop()
                op = ch
                val = self.calc(op,a,b)
                stack.append(val)
            else:
                stack.append(int(ch)) 
        return stack[-1]    