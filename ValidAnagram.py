class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False 

        counts = {}
        countt = {}

        for i in range(len(s)):
            if s[i] not in counts:
                counts[s[i]]=0
            else:
                counts[s[i]]+=1
        print(counts)
        for i in range(len(t)):
            if t[i] not in countt:
                countt[t[i]]=0
            else:
                countt[t[i]]+=1
           
                

        if counts==countt:
            return True 
        
        return False 
