from typing import List

import bisect


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[0] + x[1])
        comp = [pairs[0]]
        diff = 0
        for pair in pairs:
            if comp[-1][1] < pair[0]:
                diff = pair[0] - comp[-1][1]
                comp.append(pair)

            if comp[-1][1] > pair[1]:
                index = bisect.bisect_left(
                    list(map(lambda x: x[1], comp)), pair[1])
                if index == len(comp) - 1:
                    if diff > comp[-1][0] - pair[0]:
                        comp[index] = pair
                else:
                    comp[index] = pair
        print(comp)
        return len(comp)
