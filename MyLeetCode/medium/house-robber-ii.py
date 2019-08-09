class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        cache = [0] * len(nums)
        cache[0] = nums[0]
        cache[1] = max(nums[1], nums[0])
        
        for i in range(2, len(nums) - 1):
            cache[i] = max(cache[i-2] + nums[i], cache[i-1])

        ans = cache[len(nums) - 2]

        cache = [0] * len(nums)
        nums = nums[1:]
        cache[0] = nums[0]
        cache[1] = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            cache[i] = max(cache[i-2] + nums[i], cache[i-1])

        ans = max(ans, cache[len(nums) - 1])
        return ans
