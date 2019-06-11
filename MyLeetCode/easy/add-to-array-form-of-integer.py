class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A = list(reversed(A))
        B = [int(x) for x in reversed(list(str(K)))]
        
        """
        [0, 9, 9, 1]
        [4, 3]
        """
        result = []
        maxLen = max(len(A), len(B))
        minLen = min(len(A), len(B))
        longer = A if len(A) > len(B) else B

        over = 0

        for index in range(minLen):
            a = A[index]
            b = B[index]
            s = (a + b + over) % 10
            over = (a + b + over) // 10
            result.append(s)
        
        for index in range(minLen, maxLen):
            s = (longer[index] + over) % 10
            over = (longer[index] + over) // 10
            result.append(s)

        if over != 0:
            result.append(1)
        
        return list(reversed(result))
