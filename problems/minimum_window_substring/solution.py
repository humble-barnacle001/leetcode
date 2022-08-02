class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d_p = dict()
        for c in t:
            if c not in d_p:
                d_p[c]=0
            d_p[c]+=1
        mn = len(s)*len(t) + 96
        start = 0
        sub_start = 0
        matched = 0
        for i,x in enumerate(s):
            if x in d_p:
                d_p[x]-=1
                if d_p[x] >= 0:
                    matched += 1

            while matched == len(t):
                if mn > i - start + 1:
                    mn = i - start + 1
                    sub_start = start
                l = s[start]
                start+=1
                if l in d_p:
                    if d_p[l]==0:
                        matched -= 1
                    d_p[l]+=1
        if mn > len(s):
            return ""
        return s[sub_start:sub_start+mn]