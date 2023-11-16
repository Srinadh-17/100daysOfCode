class Solution(object):
    def equalPairs(self, grid):
        c=0
        for i in range(len(grid)):
            col=[]
            for j in range(len(grid)):
                col.append(grid[j][i])
            for k in range(len(grid)):
                if col == grid[k]:
                    c+=1
        return c