class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        temp = 0
        front = [0] * (len(nums)-k)
        back = [0] * (k)
        for i in range(len(nums)-k):
            front[temp] = nums[temp]
            temp += 1
        temp = 0
        for j in range(k):
            back[temp] = nums[len(nums)-k+temp]
            temp += 1
        temp = 0
        for t in range(len(nums)):
            if temp <= (k-1):
                nums[temp] = back[temp]
            else:
                nums[temp] = front[temp-k]
            temp += 1