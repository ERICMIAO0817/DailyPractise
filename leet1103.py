# # The isBadVersion API is already defined for you.
# # def isBadVersion(version: int) -> bool:
#
# class Solution:
#     def firstBadVersion(self, n: int) -> int:
#         left, right = 1, n
#         if isBadVersion(1):
#             return 1
#         if n == 2:
#             if isBadVersion(2) and not isBadVersion(1):
#                 return 2
#             elif isBadVersion(1) and not isBadVersion(2):
#                 return 1
#             elif isBadVersion(1) and isBadVersion(2):
#                 return 1
#         if n == 1:
#             return 1
#         while (right - left) > 1:
#             mid = (right - left) // 2 + left
#             if not isBadVersion(mid):
#                 left = mid
#             else:
#                 right = mid
#         return right

class Solution:
    def __init__(self):
        self.sq_list = []

    def numSquares(self, n: int) -> int:
        for i in range(100):
            self.sq_list.append((i+1)**2)
        left, right = 0, n - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if self.sq_list[mid] == n:
                return 1
            elif self.sq_list[mid] < n:
                left = mid + 1
            else:
                right = mid - 1
        sub = n
        while sub > 0:


    def is_in_sq(self, n:int):
        if n in self.sq_list:
            return True
        else:
            return False

    def judge(self, n:int, rang:int):
        for i in range(rang + 1):
            
