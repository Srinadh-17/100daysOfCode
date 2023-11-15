class Solution(object):
    def closeStrings(self, word1, word2):
        
        if set(word1) != set(word2): return False
        
        C1 = Counter(word1)
        C2 = Counter(word2)
        
        L1 = C1.values()
        L2 = C2.values()
        
        return sorted(L1) == sorted(L2)