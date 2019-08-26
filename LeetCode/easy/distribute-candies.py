class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        
        numOfKind = len(collections.Counter(candies))
        numOfCandies = len(candies)

        return min(numOfKind, numOfCandies//2)
