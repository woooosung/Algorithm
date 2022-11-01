class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if nums[0] >= target:
            return 0
        if nums[length-1] <= target:
            if nums[length-1]==target:
                return length-1
            return length
        temp = int((length+1)/2)
        width = temp
        while temp>0 and temp<length:
            width = int((width+1)/2)
            if nums[temp]==target:
                break
            if nums[temp] >= target and nums[temp-1] < target:
                break
            if nums[temp] > target:
                temp = temp - int((width+1)/2)
            else:
                temp = temp + int((width+1)/2)
        return temp