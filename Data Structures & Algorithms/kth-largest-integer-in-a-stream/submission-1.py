class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        self.nums = nums
        i = 0
        while i<len(self.nums):
            heapq.heappush(self.heap,self.nums[i])
            if len(self.heap)>self.k:
                heapq.heappop(self.heap)
            i = i+1
        

    def add(self, val: int) -> int:
        
        heapq.heappush(self.heap, val)
        if len(self.heap)>self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

        
