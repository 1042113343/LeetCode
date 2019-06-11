class NumArray:

    def __init__(self, nums: List[int]):
        total = []
        val = 0
        for num in nums:
            val += num
            total.append(val)
        self.total = total
        
    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.total[j]
        else:
            return self.total[j] - self.total[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
