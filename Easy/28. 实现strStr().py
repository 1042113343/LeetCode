class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle is "":
            return 0
        l = len(needle)
        for idx in range(0,len(haystack)- l+ 1):
            if haystack[idx: idx+ l] == needle:
                return idx
        return -1
