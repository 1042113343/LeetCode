class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        target,tmp  = ""
        l = 1
        flag = True
        if len(strs) == 0:
            return target
        while(flag):
            target = tmp
            tmp = strs[0][0:l]
            if len(strs) ==1:
                target = strs[0]
                break
            for i in range(len(strs)):
                if len(strs[i]) == 0 or len(strs[i]) < l:
                    flag = False
                    break
                if strs[i][0:l] != tmp:
                    flag = False
                    break
            l=l+1
        return target
