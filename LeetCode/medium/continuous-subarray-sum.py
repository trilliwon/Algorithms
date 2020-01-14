from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        comp = {0: -1}

        running_sum = 0

        for curr_index, x in enumerate(nums):
            running_sum += x
            if k != 0:
                running_sum %= k
            if running_sum in comp:
                prev_index = comp[running_sum]
                if curr_index - prev_index > 1:
                    return True
            else:
                comp[running_sum] = curr_index

        return False
