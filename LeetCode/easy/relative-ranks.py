class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        # (index, value)
        numsPair = list(enumerate(nums))
        
        # sort by value
        numsPair = sorted(numsPair, key=lambda x: x[1], reverse=True)

        # map by (value, index)
        numsPair = [(str(i + 1), x[0]) for i, x in enumerate(numsPair)]
        # Gold
        if len(numsPair) > 0:
            numsPair[0] = ("Gold Medal", numsPair[0][1])
        
        if len(numsPair) > 1:
            numsPair[1] = ("Silver Medal", numsPair[1][1])

        if len(numsPair) > 2:
            numsPair[2] = ("Bronze Medal", numsPair[2][1])

        # sort by index
        numsPair = sorted(numsPair, key=lambda x: x[1])

        return list(map(lambda x: x[0], numsPair))
        
        
