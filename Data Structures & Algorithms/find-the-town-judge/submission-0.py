class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        r=len(trust)-1

        while r>0:
            if trust[r][1]!=trust[r-1][1]:
                return -1
            r-=1
        return trust[0][1]
        