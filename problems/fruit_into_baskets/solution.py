class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        mx = 0
        start = 0
        fd = dict()
        for i, x in enumerate(fruits):
            if x not in fd:
                fd[x] = 0
            fd[x] +=1
            
            while(len(fd)>2):
                l_fruit = fruits[start]
                fd[l_fruit] -= 1
                if fd[l_fruit] == 0:
                    del fd[l_fruit]
                start += 1
            mx = max(mx, i-start+1)
            
        return mx