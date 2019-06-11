class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        target = -sys.maxsize
        val = 0
        for num in nums:
            val = max(val+num,num)
            target = max(target,val)
        return target
