class Solution:
    
    def A(self, ab, cd, ef):
        x1, y1 = ab
        x2, y2 = cd
        x3, y3 = ef
        return 1/2* abs((x1*y2 + x2*y3+ x3*y1) - (x2*y1 + x3*y2 + x1*y3))

    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        length = len(points)
        ans = 0.0
        for i in range(length):
            for j in range(length):
                for k in range(length):
                    if i == j or i == k or j == k:
                        continue
                    ans = max(ans, self.A(points[i], points[j], points[k]))
                    
        return ans       

