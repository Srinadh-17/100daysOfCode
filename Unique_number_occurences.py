class Solution(object):
    def uniqueOccurrences(self, arr):
        d={}
        for i in arr:
            if i in d.keys():
               d[i]+=1 
            else:
                d[i]=1
        if len(d)==len(set(d.values())):
            return True
        else:
            return False
        