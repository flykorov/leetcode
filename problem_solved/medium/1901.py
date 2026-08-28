class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        len_row = len(mat)
        len_col = len(mat[0])

        i = 0
        j = 0

        while(True):
            tab = [-1, -1, -1, -1]
            num = mat[i][j]

            if i-1 >=0:
                if mat[i-1][j] > num:
                    tab[0] = mat[i-1][j]

            if j-1 >= 0:
                if mat[i][j-1] > num:
                    tab[1] = mat[i][j-1]

            if i+1 < len_row:
                if mat[i+1][j] > num:
                    tab[2] = mat[i+1][j]

            if j+1 < len_col:
                if mat[i][j+1] > num:
                    tab[3] = mat[i][j+1]

            if max(tab) > num:
                imax = tab.index(max(tab))

                if imax == 0:
                    i -= 1
                if imax == 1:
                    j -= 1
                if imax == 2:
                    i += 1
                if imax == 3:
                    j += 1
            else:
                return [i, j]

