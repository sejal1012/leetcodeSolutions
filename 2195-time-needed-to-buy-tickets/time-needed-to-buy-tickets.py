from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        ticketsQ = deque(tickets)
        pointer = k
        count = 0
        while(True):
            ticketsQ[0] -= 1
            count += 1
            if(ticketsQ[0] == 0):
                if(pointer == 0):
                    break
                ticketsQ.popleft()
            else:
                element = ticketsQ.popleft()
                ticketsQ.append(element)
            if(pointer > 0):
                pointer -= 1
            else:
                pointer = len(ticketsQ) - 1
        return count
