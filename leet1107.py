class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = nums.copy()
        for index, item in enumerate(n):
            new = (index + k) % len(n)
            nums[new] = n[index]