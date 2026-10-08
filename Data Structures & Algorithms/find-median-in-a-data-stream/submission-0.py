import heapq
class MedianFinder:

    def __init__(self):
        # to insert no's from the input stream, instead of using arrays and repeatedly sorting it , we can use the concepts of min heap and max heap

        #initialize 2 heaps low (max heap) and high(min heap)
        self.low = []
        self.high = []


    def addNum(self, num: int) -> None:

        if not self.low or num<=-self.low[0]:
            heapq.heappush(self.low, -num)
        else:
            heapq.heappush(self.high,num)

        #now we also need to consider if our heaps are balanced or not
        if len(self.low)>len(self.high)+1:
            x = heapq.heappop(self.low)
            heapq.heappush(self.high,-x)
        elif len(self.high)>len(self.low):
            x = heapq.heappop(self.high)
            heapq.heappush(self.low,-x)        

    def findMedian(self) -> float:
        if len(self.low)>len(self.high):#odd no. of elements
            median = -self.low[0]
        else:
            median = (-self.low[0]+ self.high[0])/2
        return median

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()