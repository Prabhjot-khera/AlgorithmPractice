class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(', ']':'[', '}':'{'}
        stack = []
      
        for c in s:
            if c in hashmap:
                if stack and stack[-1]==hashmap[c]: 
                    stack.pop()
                    continue 
                else:
                    return False
            else:
                stack.append(c)
            
        if not stack:
          return True 
        else:
          return False

