class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums))!=len(nums)
        
#         d={}
#         for x in nums:
#             if x in d:
#                 return True
#             d[x]=x
            
#         return False
        