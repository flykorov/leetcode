# There are n teams numbered from 0 tn - 1 in a tournament.
#
# Given a 0-indexed 2D boolean matrix grid of size n * n. For all i, j that 0 <= i, j <= n - 1 and i != j team i is stronger than team j if grid[i][j] == 1, otherwise, team j is stronger than team i.
#
# Team a will be the champion of the tournament if there is no team b that is stronger than team a.
#
# Return the team that will be the champion of the tournament.


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:

        result = 0
        sum_temp = 0
        for k, i in enumerate(grid):
            a = sum(i)
            if a > sum_temp:
                sum_temp = a
                result = k

        return result
