class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        fruits = s
        mx = 0
        start = 0
        fd = dict()
        for i, x in enumerate(fruits):
            if x not in fd:
                fd[x] = 1
            else:   #swap:
                while x in fd:
                    l_fruit = fruits[start]
                    del fd[l_fruit]
                    start += 1
                fd[x] = 1  
            mx = max(mx, i-start+1)
            
        return mx