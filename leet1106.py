class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = []
        count = nums.count(0)
        # for i in range(count):
        #     temp = nums.index(0)
        #     for index in range(temp, len(nums)-1, 1):
        #         nums[index], nums[index+1] = nums[index+1], nums[index]
        for i in range(count):
            temp = nums.index(0)
            nums.pop(temp)
            nums.append(0)
            