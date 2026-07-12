class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasm=set()

        for n in nums:
            if n in hasm:
                return True
            hasm.add(n)
        return False
    