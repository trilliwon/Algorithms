"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
from functools import reduce

class Solution:

    def isAllSame(self, grid):
        return len(set(sum(grid, []))) == 1

    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """

        if self.isAllSame(grid):
            return Node(True if grid[0][0] else False, True, None, None, None, None)
        
        N = len(grid)
        topLeft = [line[0:N//2] for line in grid[0:N//2]]
        topRight = [line[N//2:N] for line in grid[0:N//2]]
        bottomLeft = [line[0:N//2] for line in grid[N//2:N]]
        bottomRight = [line[N//2:N] for line in grid[N//2:N]]
        
        return Node(True,
                    False,
                    self.construct(topLeft),
                    self.construct(topRight),
                    self.construct(bottomLeft),
                    self.construct(bottomRight))
