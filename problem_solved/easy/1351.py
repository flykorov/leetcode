# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        nb_count = 0

        for i in grid:
            for j in i:
                if j < 0:
                    nb_count += 1

        return nb_count
