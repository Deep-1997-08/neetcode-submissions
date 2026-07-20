class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res=max(nums)

        curMax=1
        curMin=1

        for n in nums:
            if n==0:
                curMax=curMin=1
                continue
            temp=n*curMax
            curMax=max(temp,n*curMin,n) # 2 
            curMin=min(temp,n*curMin,n) # 2
            res=max(curMax,res) #0 
        return res

# time o(n) o(1)