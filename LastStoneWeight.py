class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new = [-s for s in stones]
        heapq.heapify(new)

        while len(new)>1:
            one= heapq.heappop(new)
            two = heapq.heappop(new)
            if one != two:
                heapq.heappush(new, one-two)
        
        new.append(0)
        return abs(new[0])
