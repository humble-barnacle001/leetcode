class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d_p = dict()
        for c in s1:
            if c not in d_p:
                d_p[c]=0
            d_p[c]+=1
        
        start = 0
        c_dict= dict()
        for i,x in enumerate(s2):
            if x not in c_dict:
                c_dict[x] = 0
            c_dict[x]+=1
            if i - start + 1 > len(s1):
                l = s2[start]
                c_dict[l]-=1
                if c_dict[l]==0:
                    del c_dict[l]
                start+=1
            if c_dict == d_p:
                return True
        return False