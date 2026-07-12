class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSeq=set(nums)
        longest=0
        for n in nums:
            if n-1 not in numsSeq:
                length=0
                while n+length in numsSeq:
                    length+=1
                longest=max(longest,length)
        return longest