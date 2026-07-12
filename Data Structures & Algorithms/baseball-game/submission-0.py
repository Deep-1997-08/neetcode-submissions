class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]

        for n in operations:
            if n=="+":
                res.append(res[-1]+res[-2])
            elif n=="C":
                res.pop()
            elif n=="D":
                res.append(2*res[-1])
            else:
                res.append(int(n))
        return sum(res)
