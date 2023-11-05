class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        one = list(s)
        two = list(t)

        one.sort()
        two.sort()

        if one != two:
            return False
        return True
