class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        if length < 2:
            return 1

        answer = 0
        for c in [True, False]:
            comp = [nums[0]]
            compare = c
            for i in range(1, length):
                if compare and nums[i-1] < nums[i]:
                    comp.append(nums[i])
                    compare = not compare
                elif not compare and nums[i-1] > nums[i]:
                    comp.append(nums[i])
                    compare = not compare
            answer = max(answer, len(comp))
        return answer