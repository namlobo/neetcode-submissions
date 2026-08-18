class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #n cars travelling on 1 way highway
        #pos[i],speed[i] pos n speed of car i
        #dest is at pos target miles
        #non empty set of cars driving in same pos and speed
        stack = []
        fleet = len(position)
        pair = []
        for i in range(len(position)):
            pair.append([position[i],speed[i]])
        for p,s in sorted(pair)[::-1]: #reverse sorted order
            stack.append((target-p)/s) #when the car will reach the destination
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
                fleet -=1
        return fleet
