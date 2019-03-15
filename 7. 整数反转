class Solution:
    def reverse(self, x: int) -> int:
        minus =""
        reverse = ""
        if x < 0:
            minus ="-"
            x = ~x + 1
        for i in str(x):
            reverse = i + reverse
        reverse = minus + reverse
        if int(reverse) > pow(2,31) -1 or int(reverse) < pow(-2,31):
            return 0
        return int(reverse)
