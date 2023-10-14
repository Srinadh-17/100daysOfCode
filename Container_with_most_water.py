class Solution(object):
    def maxArea(self, height):
        i, j  = 0, len(height)-1
        k=0
        while i < j:
            if height[i] > height[j]:
                area = height[j] * (j-i)  
                j -= 1  
            else:
                area = height[i] * (j-i)
                i += 1
            if area > k:
                k = area  
        return k

        
        