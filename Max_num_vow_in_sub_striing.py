class Solution(object):
    def maxVowels(self, s, k):
        a = {'a', 'e', 'i', 'o', 'u'}
        l,c,res=0,0,0
        for i in range((len(s))):
            c+=1 if s[i] in a else 0
            if i-l+1>k:
                c-=1 if s[l] in a else 0
                l+=1
            res=max(res,c)
        return res
    