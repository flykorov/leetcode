# Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        if len(bin(left)) != len(bin(right)):
            return 0

        resultat = ""
        cont = False

        for i, j in zip(bin(left)[2:], bin(right)[2:]):
            if i != j or cont:
                cont = True
                resultat += "0"
            else:
                resultat += i

        return int(resultat, 2)
