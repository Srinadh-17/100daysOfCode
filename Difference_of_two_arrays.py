class Solution(object):
    def findDifference(self, nums1, nums2):
        answer=[]
        answer1=[]
        for i in (set(nums1)):
            if i in nums2:
                pass
            else:
                answer.append(i)
        for i in (set(nums2)):
            if i in nums1:
                pass
            else:
                answer1.append(i)
        return [answer,answer1]

        