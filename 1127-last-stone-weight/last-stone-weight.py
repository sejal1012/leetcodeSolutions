import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stonesMax = [-stone for stone in stones]
        heapq.heapify(stonesMax)
        while(len(stonesMax) > 1):
            largest1 = -heapq.heappop(stonesMax)
            largest2 = -heapq.heappop(stonesMax)
            if(largest1 > largest2):
                heapq.heappush(stonesMax, -(largest1 - largest2))
        if(len(stonesMax)):
            return -stonesMax[0]
        else:
            return 0