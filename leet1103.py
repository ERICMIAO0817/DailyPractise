# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        if isBadVersion(1):
            return 1
        if n == 2:
            if isBadVersion(2) and not isBadVersion(1):
                return 2
            elif isBadVersion(1) and not isBadVersion(2):
                return 1
            elif isBadVersion(1) and isBadVersion(2):
                return 1
        if n == 1:
            return 1
        while (right - left) > 1:
            mid = (right - left) // 2 + left
            if not isBadVersion(mid):
                left = mid
            else:
                right = mid
        return right