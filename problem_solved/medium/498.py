# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        i = 0
        j = 0

        m = len(mat)
        n = len(mat[0])

        tab = []

        up = True

        for k in range(m * n):
            tab.append(mat[i][j])

            # print(i, j)

            if up:
                if i - 1 >= 0 and j + 1 < n:
                    j += 1
                    i -= 1
                else:
                    if j + 1 >= n:
                        i += 1
                        up = False
                    else:
                        j += 1
                        up = False
            else:
                if i + 1 < m and j - 1 >= 0:
                    j -= 1
                    i += 1
                else:
                    if i + 1 >= m:
                        j += 1
                        up = True
                    else:
                        i += 1
                        up = True

        return tab
