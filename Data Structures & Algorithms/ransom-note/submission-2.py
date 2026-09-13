class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countR=Counter(ransomNote)
        countM=Counter(magazine)

        for c in countR:
            if countR[c]>countM[c]:
                return False
        return True