class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        results =[]

        dicti = {}

        for i in nums:
            dicti[i]=0

        for i in nums:
            dicti[i]+=1
        
        sortedval = {k: v for k, v in sorted(dicti.items(), key= lambda v:v[1])}

        new = list(sortedval.keys())
        
        for i in range(1,k+1):
            results.append(new[-i])
        return results
