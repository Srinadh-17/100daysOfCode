class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        a=len(citations)
        for i in range(len(citations)):
            if citations[i]>=a:
                break
            else:
                a-=1
        return a