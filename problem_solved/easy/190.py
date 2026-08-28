class Solution:
    def reverseBits(self, n: int) -> int:
        bit = [0 for i in range(32)]

        j = 31
        while n != 0 and j >= 0:
            bit[j] = n % 2
            n = n // 2
            j -= 1

        res = 0
        pui = 0
        for i in bit:
            res += i * 2**pui
            pui += 1

        return res
