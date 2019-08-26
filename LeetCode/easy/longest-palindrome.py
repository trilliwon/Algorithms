class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        counter = collections.Counter()
        for c in s:
            counter[c] += 1

        ans = 0

        for key, value in counter.items():

            if value % 2 == 0:
                ans += value
            else:
                if value > 2:
                    ans += (value-1)
                    counter[key] = 1

        for _, value in counter.items():
            if value == 1:
                ans += 1
                break
        return ans
