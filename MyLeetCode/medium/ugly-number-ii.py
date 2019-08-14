class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # only include

        result = [1]
        i, j, k = 0, 0, 0
        
        while len(result) < n:
            x = min(result[i] * 2, result[j] * 3, result[k] * 5)
            result.append(x)
            
            if x == result[i] * 2:
                i += 1
            if x == result[j] * 3:
                j += 1
            if x == result[k] * 5:
                k += 1

        return result[n-1]
