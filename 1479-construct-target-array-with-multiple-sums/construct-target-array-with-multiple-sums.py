import heapq
class Solution:
    def isPossible(self, target: list[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1
        maxheap = [-num for num in target]
        heapq.heapify(maxheap)
        total = -sum(maxheap)
        while(maxheap[0] != -1):
            largest = -maxheap[0]
            other = total - largest
            if(largest <= other):
                return False
            if(other == 1):
                return True
            rem = largest % other
            if(rem == 0):
                return False
            heapq.heapreplace(maxheap, -rem)
            total = other + rem
        return True
