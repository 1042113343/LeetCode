class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        limit_x, limit_y = 0, 0
        if x > 1:
            while(x ** limit_x <= bound):
                limit_x +=1
        else:
            limit_x = 1
        if y > 1:
            while(y ** limit_y <= bound):
                limit_y +=1
        else:
            limit_y = 1
        ans = set()
        for i in range(0, limit_x):
            for j in range(0, limit_y):
                v = x ** i + y ** j
                if v <= bound:
                    ans.add(v)
        return list(ans)
