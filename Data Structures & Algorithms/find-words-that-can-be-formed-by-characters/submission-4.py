class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        countC=Counter(chars)
        res=0

        for w in words:
            cur_word=Counter(w)
            good=True
            for c in w:
                if cur_word[c]>countC[c]:
                    good=False
                    break
            if good:
                res+=len(w)
        return res