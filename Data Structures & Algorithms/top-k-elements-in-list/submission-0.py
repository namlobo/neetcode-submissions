class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #since they have asked to maintain the freq , using hashmap seems like the optimal soln
        count = {}
        for i in nums:
            count[i] = count.get(i,0)+1 #build hashmap counting the frequency of each number, where the no. is the key and the values hold the freq of the number
        newcount = list(count.items())
        newcount.sort(key=lambda x:x[1], reverse = True)
        final = []
        for i in range(k):
            final.append(newcount[i][0])
        return final
        