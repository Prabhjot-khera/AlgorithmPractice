from string import *
class Solution:
    def isPalindrome(self, s: str) -> bool:

        news=s.lower()

        chars = list(string.ascii_lowercase)

        str2=[]

        for i in range(10):
            chars.append(str(i))
        
        for char in news:
            if char in chars:
                str2.append(char)
        
        start=0
        end=-1

        for i in range(len(str2)):
            if str2[start] != str2[end]:
                return False 
            start+=1
            end-=1
        return True 
