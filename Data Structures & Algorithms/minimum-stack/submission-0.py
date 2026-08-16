class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = [] #maintain another stack called min stack whose top element stores the min value from the stack
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.minstack: 
            self.minstack.append(value)
        else:
            self.minstack.append(min(value,self.minstack[-1]))
            #while appending a new value into your stack, check if the value currently exists in minstack, if not then append the min of curr val and top of minstack onto top of min stack
        
        

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]


