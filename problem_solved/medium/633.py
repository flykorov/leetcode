# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.


class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        for i in range(46341):
            if c - i**2 < 0:
                return False

            if sqrt(c - i**2) % 1 == 0:
                return True

        return False
