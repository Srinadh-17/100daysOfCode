class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        for i in range(len(s)-1,-1,-1):
            if s[i]==" ":
                continue
            else:
                count+=1
                if s[i-1]==" " or i==len(s):
                    break
        return count
        