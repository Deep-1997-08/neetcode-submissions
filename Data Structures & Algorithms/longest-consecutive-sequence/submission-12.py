class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numseq=set(nums)
        longest=0
        for n in nums:
            if n-1 not in numseq:
                length=0
                while n+length in numseq:
                    length+=1
                longest=max(longest,length)
        return longest