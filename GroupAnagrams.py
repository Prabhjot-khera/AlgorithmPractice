from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dicti =defaultdict(list)  
        result =[]

        for s in strs:
            new = tuple(sorted(s))
            dicti[new].append(s)

        for i in dicti.values():
            result.append(i)
        return result
