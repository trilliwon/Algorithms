class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        
        dict1 = { x:index for index, x in enumerate(list1) }
        dict2 = { x:index for index, x in enumerate(list2) }
        
        common = {}
        for key, index in dict1.items():
            if key in dict2:
                common[key] = dict2[key] + index
        
        sortedCommon = sorted(common, key = common.get)
        
        indexSum = common[sortedCommon[0]]
        ans = []
        for c in sortedCommon:
            if common[c] == indexSum:
                ans.append(c)
            else:
                break
        return ans
