class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = ""
        for i in str(x):
            reverse = i + reverse
        return True if reverse == str(x) else False
