class Solution:
    def findShortestSubArray(self, nums):
        """
        Time  : O(N)
        Space : O(N)
        
        :type nums: List[int]
        :rtype: int
        """
        
        """
        - find maximum frequency elements index range i to j
        [1,2,2,3,1,4,2]
                     ^
        { 1:(0, 4), 2:(1, 6), 3:(3, 3), 4:(5, 5) }
        
        max = 2
        """
        if not nums:
            return 0

        comp_map = {}
        counter = collections.Counter()
        
        # O(N)
        for i, x in enumerate(nums):
            counter[x] += 1
            if x in comp_map:
                comp_map[x] = (comp_map[x][0], i)
            else:
                comp_map[x] = (i, i)
        
        # O(K) : len(unique nums) = K, K <= N
        max_freq = max([ v for _, v in counter.items()])
        max_freq_elems = []
        
        # O(K)
        for k, v in counter.items():
            if v == max_freq:
                max_freq_elems.append(k)
        
        ans = len(nums) + 1
        
        # O(N)
        for e in max_freq_elems:
            ans = min((comp_map[e][1] - comp_map[e][0] + 1), ans)
        return ans
