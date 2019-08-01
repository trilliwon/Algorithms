class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 0:
            return 0

        maxLen = len(triangle)
        cache = [[0 for _ in range(maxLen)] for _ in range(maxLen)]
        check = [[False for _ in range(maxLen)] for _ in range(maxLen)]

        cache[0][0] = triangle[0][0]
        check[0][0] = True

        for i in range(maxLen - 1):
            for index, value in enumerate(triangle[i]):

                left = cache[i][index] + triangle[i + 1][index]

                if check[i + 1][index] == True:
                    cache[i + 1][index] = min(cache[i + 1][index], left)
                else:
                    cache[i + 1][index] = left
                    check[i + 1][index] = True

                right = cache[i][index] + triangle[i + 1][index + 1]

                if check[i + 1][index + 1] == True:
                    cache[i + 1][index + 1] = min(cache[i + 1][index + 1], right)
                else:
                    cache[i + 1][index + 1] = right
                    check[i + 1][index + 1] = True

        return min(cache[maxLen - 1])
