class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        answer = nums[0]
        minValue = nums[0]
        maxValue = nums[0]
        
        for x in nums[1:]:
            tMin = min(x, x * minValue, x * maxValue)
            tMax = max(x, x * minValue, x * maxValue)
            minValue = tMin
            maxValue = tMax
            answer = max(answer, x, maxValue, minValue)

        return answer
