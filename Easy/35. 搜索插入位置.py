class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums is None:
            return 0
        for i in range(0,len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
