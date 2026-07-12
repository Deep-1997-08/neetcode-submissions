class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=[[] for i in range(len(nums)+1)]
        count={}

        for n in nums:
            count[n]=count.get(n,0)+1
        for i,c in count.items():
            freq[c].append(i)
        
        res=[]
        for i in range(len(freq)-1,-1,-1):
            for c in freq[i]:
                res.append(c)
                if len(res)==k:
                    return res
    