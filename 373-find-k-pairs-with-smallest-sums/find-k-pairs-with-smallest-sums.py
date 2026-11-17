import heapq
class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        numHeap = []
        for i,n in enumerate(nums2):
            heapq.heappush(numHeap, (n+nums1[0], 0, i))
        result = []
        while(len(result) < k):
            res = heapq.heappop(numHeap)
            result.append([nums1[res[1]], nums2[res[2]]])
            if(res[1] + 1 < len(nums1)):
                heapq.heappush(numHeap, (nums1[res[1]+1]+nums2[res[2]], res[1]+1, res[2]))
        return result