class Solution(object):
    def longestOnes(self, nums, k):
        t,j,c,res=0,0,0,0
        for i in range(len(nums)):
            while t<len(nums) and j<=k:
                if nums[t]==1:
                    t+=1
                    c+=1
                else:
                    if j==k:
                        break
                    j+=1
                    t+=1
                    c+=1
            res=max(res,c)
            if t==len(nums):
                break
            if nums[i]==0:
                j-=1
            c-=1    
        return res
        
        


