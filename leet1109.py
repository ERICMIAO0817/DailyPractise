class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #         s[:] = s[::-1]
        left = 0
        right = len(s) - 1
        for i in range(len(s) // 2):
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
