class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d_p = dict()
        for c in p:
            if c not in d_p:
                d_p[c]=0
            d_p[c]+=1
        result = []
        start = 0
        c_dict= dict()
        for i,x in enumerate(s):
            if x not in c_dict:
                c_dict[x] = 0
            c_dict[x]+=1
            if i - start + 1 > len(p):
                l = s[start]
                c_dict[l]-=1
                if c_dict[l]==0:
                    del c_dict[l]
                start+=1
            if c_dict == d_p:
                result.append(start)
        return result