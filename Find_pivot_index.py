class Solution(object):
    def pivotIndex(self, nums):
        for i in range(1,len(nums)+1,1):
            a=sum(nums[:i-1])
            b=sum(nums[i::])
            if a==b:
                return i-1
        return -1
        