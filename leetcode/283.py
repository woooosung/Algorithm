class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = 0
        
        for i in range(len(nums)):
            pivot = nums[i]
            if pivot != 0:
                nums[temp], nums[i] = nums[i], nums[temp]
                temp += 1