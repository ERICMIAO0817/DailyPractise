class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index, _ in enumerate(numbers):
            to_find = target - _
            res = self.search(numbers[index+1:], to_find)
            if res != -1:
                return index+1, res+1+index

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            num = nums[mid]
            if num == target:
                return mid
            elif num > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1