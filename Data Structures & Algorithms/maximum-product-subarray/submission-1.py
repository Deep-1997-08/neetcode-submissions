class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)

        curMin,curMax=1,1

        for n in nums:
            if n==0:
                curMax,curMin=1,1
                continue
            temp=n*curMax
            curMax=max(temp,n*curMin,n)
            curMin=min(temp,n*curMin,n)
            res=max(curMax,res)
        return res