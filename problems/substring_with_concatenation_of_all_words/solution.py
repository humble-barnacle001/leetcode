class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        w_d = dict()
        for word in words:
            if word not in w_d:
                w_d[word] = 0
            w_d[word] += 1
        wl = len(words[0])
        wc = len(words)
        res = []
        for i in range(len(s) - wc*wl +1):
            seen = dict()
            for j in range(wc):
                x = i + j*wl
                t = s[x:x+wl]
                
                if t not in w_d:
                    break
                if t not in seen:
                    seen[t] = 0
                seen[t]+=1
                
                if seen[t] > w_d[t]:
                    break
                    
                if j == wc -1:
                    res.append(i)
        return res
            