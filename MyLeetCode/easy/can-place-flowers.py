class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """

        Time  : O(N)
        Space : O(1)

        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        if len(flowerbed) <= 2:
            if sum(flowerbed) == 1:
                return n == 0
            return n <= 1
            
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1

        if flowerbed[len(flowerbed)-2] == 0 and flowerbed[len(flowerbed)-1] == 0:
            flowerbed[len(flowerbed)-1] = 1
            n-= 1

        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1

        return n <= 0
