class Solution(object):
    def largestAltitude(self, gain):
        ans=[0]
        for i in range(len(gain)):
            ans.append(ans[i]+gain[i])            
        return max(ans)
        