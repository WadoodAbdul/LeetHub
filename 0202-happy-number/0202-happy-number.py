class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = self.sumOfSqares(n)
            if n == 1:
                return True
        return False
    
    def sumOfSqares(self, n):
        res = 0
        while n:
            n, d = divmod(n, 10)
            res += d * d
        return res
        