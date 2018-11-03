class Solution:
    
    def distance(self, i, j):
        return (i[0] - j[0])**2 + (i[1] - j[1])**2
        
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        numOfPoints = len(points)
        ans = 0
        for i in range(numOfPoints):
            counter = collections.Counter([self.distance(points[i], points[j]) for j in range(numOfPoints) if i != j])
            frequency = [i*(i-1) for i in list(counter.values())]
            ans += sum(frequency)
            
        return ans
