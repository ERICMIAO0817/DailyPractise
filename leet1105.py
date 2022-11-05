class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = map(abs, nums)
        nums = map(lambda x: x ** 2, nums)
        return sorted(nums)
