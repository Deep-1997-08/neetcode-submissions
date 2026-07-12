class Solution:
    def mySqrt(self, x: int) -> int:
        n=0
        while True:
            if (n*n)<=x<((n+1)*(n+1)):
                return n
            n+=1