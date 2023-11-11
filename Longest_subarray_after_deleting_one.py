class Solution(object):
    def longestSubarray(self, nums):
        if 0 not in nums[::]:
            return (len(nums)-1)
        else:
            t,j,c,res=0,0,0,0
            for i in range(len(nums)):
                while t<len(nums) and j<2:
                    if nums[t]==1:
                        t+=1
                        c+=1
                    else:
                        t+=1
                        j+=1
                        if j==2:
                            break
                res=max(res,c)
                if nums[i]==0:
                    j-=1
                else:
                    c-=1    
            return res
        
          
        
        