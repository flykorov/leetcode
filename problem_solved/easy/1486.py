class Solution:
    def xorOperation(self, n: int, start: int) -> int:

        tab = [start + 2 * i for i in range(1, n)]
        
        result = start

        for i in tab:

            result ^= i
        
        return result

