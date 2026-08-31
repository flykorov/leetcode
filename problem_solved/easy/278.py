# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
#
# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        if isBadVersion(1):
            return 1

        return self.dichotomie(n//2, n, 1)
    

    def dichotomie(self, i: int, min_is_true: int, max_is_false: int) -> int:

        if min_is_true - 1 == max_is_false:
            return min_is_true

        if isBadVersion(i):
            min_is_true = i
        else:
            max_is_false = i
            
        i = min_is_true - (min_is_true - max_is_false) // 2

        return self.dichotomie(i, min_is_true, max_is_false)
