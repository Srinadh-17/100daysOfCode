class Solution(object):
    def threeSum(self, nums):
        k=[]
        nums.sort()
        for a in xrange(len(nums)-2):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            i, j = a+1, len(nums)-1
            while i < j:
                sum = nums[a] + nums[i] + nums[j]
                if sum < 0:
                    i+= 1
                elif sum>0:
                    j-= 1
                else :
                    k.append((nums[a],nums[i],nums[j]))
                    while i < j and nums[i] == nums[i+1]:
                        i += 1
                    while i < j and nums[j] == nums[j-1]:
                        j -= 1
                    i+=1; j-=1
        return k
        