class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, x in enumerate(nums):
            if x not in d:
                d[x] = []
            d[x].append(i)
            
        for k in d.keys():
            r = target - k
            if r in d:
                t = 0
                if r == k:
                    if len(d[r]) == 1:
                        continue
                    else:
                        t = 1
                return [d[k][0], d[r][t]]
            