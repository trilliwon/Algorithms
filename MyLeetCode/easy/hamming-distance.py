class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int

        """
        x = format(x, 'b')[::-1]
        for _ in range(31 - len(x)):
            x += ('0')
        y = format(y, 'b')[::-1]
        for _ in range(31 - len(y)):
            y += ('0')
        return sum(el1 != el2 for el1, el2 in zip(x[::-1], y[::-1]))
