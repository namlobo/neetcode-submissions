class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #pair: [temp,index]
        n =len(temperatures)
        result = [0]*n
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackT,stackI = stack.pop()
                result[stackI] = i-stackI
            stack.append([t,i])
        return result
        