class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ['' for _ in range(len(indices))]

        for i, k in zip(s, indices):
            res[k] = i

        p = ""

        for i in res:
            p += i
        
        return p
