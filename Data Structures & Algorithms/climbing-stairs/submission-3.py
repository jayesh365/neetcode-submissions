class Solution:
    def climbStairs(self, n: int) -> int:
        # fib
        one, two = 1, 1

        for i in range(n-1):
            curr = one
            one = one+two
            two = curr
        
        return one
