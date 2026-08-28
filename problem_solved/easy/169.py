class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        c = 0
        m = 0

        for i in nums:
            if c == 0:
                m = i
                c += 1
            elif m == i:
                c += 1
            else:
                c -= 1

        return m
