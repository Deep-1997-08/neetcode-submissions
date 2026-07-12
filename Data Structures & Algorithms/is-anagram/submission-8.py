class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sCount, tCount = {}, {}

        for c in range(len(s)):
            sCount[s[c]] = sCount.get(s[c],0)+1
            tCount[t[c]] = tCount.get(t[c],0)+1
        for c in s:
            if sCount[c]!=tCount.get(c,0):
                return False
        
        return True