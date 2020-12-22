class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        res=[]
        n=len(nums)
        for i in range(n-k+1):
            temp=nums[i:i+k]
            temp.sort()
            # print(temp)
            if(k%2==0):
                res.append((temp[k//2]+temp[(k-1)//2])/2.0)
            else:
                res.append(temp[k//2])
            
        return res
        