class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest_seq = 0

        for n in nums:
            if (n-1) not in s:
                length = 0
                while (n+ length) in s:
                    length +=1
                longest_seq = max(length, longest_seq)
        
        return longest_seq


        
