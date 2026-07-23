class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        counts,countt={},{}

        for c in range(len(s)):
            counts[s[c]]=counts.get(s[c],0)+1
            countt[t[c]]=countt.get(t[c],0)+1
        
        for c in counts:
            if counts[c]!=countt.get(c,0):
                return False
        
        return True

