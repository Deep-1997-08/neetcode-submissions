class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        res={}

        for i,n in enumerate(nums):
            if n in res and abs(res[n]-i)<=k:
                return True
            res[n]=i
        return False
