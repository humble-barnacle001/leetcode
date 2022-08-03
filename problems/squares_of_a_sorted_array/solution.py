class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
#         t = list(map(lambda x: x*x, nums))
#         t.sort()        
#         return t
        d = dict()
        for x in nums:
            if abs(x) not in d:
                d[abs(x)] = 0
            d[abs(x)] += 1
        t=list(d.keys())
        t.sort()
        
        t2 = []
        for x in t:
            for _ in range(d[x]):
                t2.append(x*x)
        return t2
        