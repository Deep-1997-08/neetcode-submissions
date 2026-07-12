class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSeq=set(nums)
        res=0

        for n in numSeq:
            if n-1 not in numSeq:
                length=0
                while n+length in numSeq:
                    length+=1
                res=max(res,length)
        return res