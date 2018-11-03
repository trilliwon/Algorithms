import bisect

class Solution:
    def findRadius(self, houses, heaters):
        """
        
        Binary Search
        
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        
        heaters.sort()
        numOfHeaters = len(heaters)
        ans = 0
        
        for house in houses:
            index = bisect.bisect_left(heaters, house)
            if index == numOfHeaters:
                ans = max(ans, house - heaters[-1])
            elif index == 0:
                ans = max(ans, heaters[0] - house)
            else:
                ans = max(ans, min(heaters[index] - house, house - heaters[index-1]))
        return ans
        
