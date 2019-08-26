class Solution:
    def findPairs(self, nums, k):
        """
        - array is not sorted
        - edge case 1 : k = 0 
        - edge case 2 : k < 0
        
        :Time: O(N)
        :Space: O(N)

        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        if k < 0:
            return 0

        cache = set()
        comp = set()
        cache_same_pair = set()

        for n in nums:
            if k == 0 and n in comp:
                cache_same_pair.add(n)
                continue

            if n-k in comp:
                cache.add((n-k, n))
                cache.add((n, n-k))

            if n+k in comp:
                cache.add((n+k, n))
                cache.add((n, n+k))

            comp.add(n)

        return len(cache)//2 + len(cache_same_pair)
