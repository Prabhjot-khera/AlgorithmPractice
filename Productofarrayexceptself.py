class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = 1

        res = [1]

        for i in range(1,len(nums)):
            prefix*=nums[i-1]
            res.append(prefix)

        post = 1

        for i in range(len(nums)-2,-1,-1):
            post*=nums[i+1]
            res[i]*=post

        return res
