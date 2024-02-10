class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new = s.split(" ")

        print(new[::-1])

        for i in new[::-1]:
            if i!='':
                return len(i)
